import os
import json
import uuid
import xml.etree.ElementTree as ET
import logging
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine import run_scan, REPORT_DIR
import redis
from rq import Queue

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# RQ Setup
redis_url = os.getenv('REDIS_URL', 'redis://redis:6379')
redis_conn = redis.from_url(redis_url)
q = Queue(connection=redis_conn)

app = FastAPI()

PROFILE_TOOLS = {
    "white": {
        "Nmap": "nmap_white.xml",
        "TestSSL": "testssl.json",
        "Dirsearch": "dirsearch.json",
        "Nikto": "nikto_white.json",
        "WhatWeb": "whatweb.json",
        "Nuclei": "nuclei_white.json",
        "Arjun": "arjun.json",
        "Dalfox": "dalfox.json",
        "Wafw00f": "wafw00f.json",
        "DNSRecon": "dnsrecon.json"
    },
    "gray": {
        "Nmap": "nmap_gray.xml",
        "WPScan": "wpscan.json",
        "ZAP Baseline": "zap.json",
        "SSLyze": "sslyze.json"
    },
    "black": {
        "Nmap": "nmap_black.xml",
        "Nuclei": "nuclei.json",
        "Nikto": "nikto_black.json"
    }
}



class ScanRequest(BaseModel):
    ip: str
    category: str


@app.post("/scan")
async def create_scan(req: ScanRequest):
    try:
        # Generate UID here so we can return it immediately
        uid = uuid.uuid4().hex
        
        # Enqueue the scan job to RQ with 30 minute timeout
        job = q.enqueue(run_scan, req.ip, req.category, uid, job_timeout=1800)
        logger.info(f"Enqueued scan job {job.id} for target {req.ip}, UID: {uid}")
        
        return {
            "status": "started",
            "scan_id": uid,
            "job_id": job.id
        }
    except Exception as e:
        logger.error(f"Error starting scan job: {e}")
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.get("/scan/{scan_id}")
async def get_scan_status(scan_id: str):
    """Get real-time scan status from Redis"""
    try:
        # Check metadata in Redis
        meta = redis_conn.hgetall(f"scan:{scan_id}:meta")
        if not meta:
            return {"status": "not_found", "scan_id": scan_id}
        
        status = meta.get(b"status", b"running").decode('utf-8')
        
        # Check individual services status from logs logic (optional, but UI uses it)
        # We can reconstruct it from the logs in Redis
        services_status = {}
        logs = redis_conn.lrange(f"scan:{scan_id}:logs", 0, -1)
        
        for line_bytes in logs:
            line = line_bytes.decode('utf-8')
            if "🚀 Starting" in line:
                parts = line.split("Starting ")
                if len(parts) > 1:
                    svc = parts[1].split("(")[0].strip().split("...")[0].strip()
                    services_status[svc] = {"status": "running", "completed": False}
            elif "✅" in line and "completed" in line:
                parts = line.split("] ✅ ")
                if len(parts) > 1:
                    svc = parts[1].split(" completed")[0].strip()
                    services_status[svc] = {"status": "completed", "completed": True}
            elif "❌" in line and "failed" in line:
                 parts = line.split("] ❌ ")
                 if len(parts) > 1:
                    svc = parts[1].split(" failed")[0].strip()
                    services_status[svc] = {"status": "failed", "completed": True}

        return {
            "status": status,
            "scan_id": scan_id,
            "services": services_status
        }
    except Exception as e:
        logger.error(f"Error getting scan status: {e}")
        return {"status": "error", "scan_id": scan_id, "error": str(e)}


@app.get("/scan/{scan_id}/logs")
def get_scan_logs(scan_id: str):
    """Get real-time scan logs from Redis"""
    try:
        logs_bytes = redis_conn.lrange(f"scan:{scan_id}:logs", 0, -1)
        logs = [log.decode('utf-8') for log in logs_bytes]
        if not logs:
             return {"scan_id": scan_id, "logs": [], "message": "No logs found"}
             
        return {
            "scan_id": scan_id,
            "logs": logs,
            "total_lines": len(logs)
        }
    except Exception as e:
        return {"scan_id": scan_id, "logs": [], "error": str(e)}


@app.get("/scan/{scan_id}/results")
def get_scan_results(scan_id: str):
    """Get scan results from Redis"""
    
    # Get metadata for target info
    meta_bytes = redis_conn.hgetall(f"scan:{scan_id}:meta")
    meta = {k.decode('utf-8'): v.decode('utf-8') for k, v in meta_bytes.items()}
    target = meta.get("target", "unknown")
    category = meta.get("category", "unknown")
    
    results = {
        "scan_id": scan_id,
        "target": target,
        "scan_type": category,
        "timestamp": meta.get("started_at", datetime.now().isoformat()),
        "findings": []
    }

    # Helper to get content from Redis
    def get_content(service_name):
        content_bytes = redis_conn.get(f"scan:{scan_id}:result:{service_name}")
        return content_bytes.decode('utf-8') if content_bytes else None

    # 1. Nuclei (Critical)
    for nuclei_svc in ["nuclei", "nuclei_white"]:
        content = get_content(nuclei_svc)
        if content:
            for line in content.splitlines():
                if not line.strip(): continue
                try:
                    finding = json.loads(line)
                    results["findings"].append({
                        "id": f"nuc-{len(results['findings'])}",
                        "title": finding.get("info", {}).get("name", "Unknown Vuln"),
                        "severity": finding.get("info", {}).get("severity", "Low").capitalize(),
                        "description": f"Template: {finding.get('template-id')}\nMatcher: {finding.get('matcher-name', 'N/A')}\nExtracted: {finding.get('extracted-results', [])}"
                    })
                except json.JSONDecodeError:
                    pass

    # 2. Nikto
    for nikto_svc in ["nikto_white", "nikto_black"]:
        content = get_content(nikto_svc)
        if content:
            try:
                data = json.loads(content)
                items = []
                if isinstance(data, list):
                    for entry in data:
                        items.extend(entry.get("vulnerabilities", []))
                else:
                    items = data.get("vulnerabilities", [])
                
                for item in items:
                    if item.get("firewall") != "None":
                        results["findings"].append({
                            "id": f"waf-{len(results['findings'])}",
                            "title": f"WAF Detected: {item.get('firewall')}",
                            "severity": "Info",
                            "description": f"Target is protected by {item.get('firewall')} ({item.get('manufacturer', 'N/A')})"
                        })
        except Exception as e:
            logger.error(f"Error reading wafw00f file: {e}")

    # 11. DNSRecon
    dns_path = os.path.join(data_dir, "dnsrecon.json")
    if os.path.exists(dns_path):
        try:
            with open(dns_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    results["findings"].append({
                        "id": f"dns-{len(results['findings'])}",
                        "title": f"DNS Record: {item.get('type')}",
                        "severity": "Info",
                        "description": f"Name: {item.get('name')}\nValue: {item.get('address') or item.get('exchange') or item.get('strings') or 'N/A'}"
                    })
        except Exception as e:
            logger.error(f"Error reading dnsrecon file: {e}")


    # Placeholder for counts if findings empty
    if not results["findings"]:
        # Check if we at least have files but no findings
        if results["raw_files"]:
            results["findings"].append({
                "id": "info-1",
                "title": "Scan Finished",
                "severity": "Info",
                "description": f"Scan completed. Found files: {', '.join(results['raw_files'])}. No critical vulnerabilities were automatically flagged."
            })
        else:
            results["findings"].append({
                "id": "info-1",
                "title": "Scan Incomplete",
                "severity": "Info",
                "description": "The scan finished or was interrupted without producing output files."
            })

    # Final pass to ensure severity is capitalized correctly for frontend
    for f in results["findings"]:
        f["severity"] = f["severity"].capitalize()
        # Map "Informational" or anything else to "Info" for consistency if needed
        if f["severity"] == "Informational":
            f["severity"] = "Info"

    return results

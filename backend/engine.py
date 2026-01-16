import subprocess
import uuid
import os
import json
import asyncio
import time
from datetime import datetime

BASE_DIR = "/app"
COMPOSE_FILE = f"{BASE_DIR}/compose/docker-compose.string.yml"
REPORT_DIR = f"{BASE_DIR}/reports"

# Define services for each profile
PROFILE_SERVICES = {
    "white": ["nmap_white", "testssl", "dirsearch", "nikto_white", "whatweb", "nuclei_white", "arjun", "dalfox", "wafw00f", "dnsrecon"],
    "gray": ["nmap_gray", "wpscan", "zap", "sslyze"],
    "black": ["nmap_black", "nuclei", "nikto_black"]
}


def log_scan(uid: str, message: str):
    """Log scan progress to a file"""
    log_file = f"{REPORT_DIR}/{uid}/data/scan.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{uid}] {message}")


async def run_service_async(service_name: str, env_vars: dict, uid: str) -> tuple:
    """Run a single service asynchronously"""
    log_scan(uid, f"🚀 Starting {service_name}...")
    start_time = time.time()
    
    try:
        # Run service in detached mode
        process = await asyncio.create_subprocess_exec(
            "docker", "compose", "-f", COMPOSE_FILE, 
            "run", "--rm", service_name,
            env=env_vars,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        duration = time.time() - start_time
        
        if process.returncode == 0:
            log_scan(uid, f"✅ {service_name} completed in {duration:.1f}s")
            return (service_name, True, None)
        else:
            error_msg = stderr.decode()[:200] if stderr else "Unknown error"
            log_scan(uid, f"❌ {service_name} failed: {error_msg}")
            return (service_name, False, error_msg)
            
    except Exception as e:
        duration = time.time() - start_time
        log_scan(uid, f"💥 {service_name} crashed after {duration:.1f}s: {str(e)}")
        return (service_name, False, str(e))


async def run_all_services_parallel(services: list, env_vars: dict, uid: str):
    """Run all services in parallel"""
    log_scan(uid, f"📋 Running {len(services)} services in parallel...")
    
    # Create tasks for all services
    tasks = [run_service_async(svc, env_vars, uid) for svc in services]
    
    # Wait for all to complete
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Summary
    successful = sum(1 for r in results if isinstance(r, tuple) and r[1])
    failed = len(results) - successful
    
    log_scan(uid, f"📊 Summary: {successful} succeeded, {failed} failed")
    return results


def run_scan(target: str, category: str, uid: str = None) -> str:
    if not uid:
        uid = uuid.uuid4().hex
    
    # Internal path (container view)
    data_dir_internal = f"{REPORT_DIR}/{uid}/data"
    os.makedirs(data_dir_internal, exist_ok=True)
    
    # Host path (for DinD)
    host_reports_path = os.environ.get("HOST_REPORTS_PATH", f"{os.getcwd()}/reports")
    host_data_dir = f"{host_reports_path}/{uid}/data"

    # Save metadata for UI tracking
    with open(f"{data_dir_internal}/meta.json", "w") as f:
        json.dump({"target": target, "category": category, "uid": uid}, f)

    # Sanitize and parse target
    target_raw = target.strip()
    target_domain = target_raw.replace("https://", "").replace("http://", "").split('/')[0].split(':')[0]
    target_url = target_raw if (target_raw.startswith("http://") or target_raw.startswith("https://")) else f"http://{target_raw}"

    env_vars = os.environ.copy()
    env_vars["TARGET"] = target_raw
    env_vars["TARGET_URL"] = target_url
    env_vars["TARGET_DOMAIN"] = target_domain
    env_vars["HOST_DATA_DIR"] = host_data_dir

    # Get services for this profile
    services = PROFILE_SERVICES.get(category, [])
    
    log_scan(uid, f"🎯 Starting {category.upper()} scan for {target}")
    log_scan(uid, f"📦 Services: {', '.join(services)}")
    
    # Run all services in parallel
    try:
        asyncio.run(run_all_services_parallel(services, env_vars, uid))
    except Exception as e:
        log_scan(uid, f"💥 Scan execution failed: {str(e)}")
        raise RuntimeError(f"Scan failed: {str(e)}")

    # Mark scan as completed
    log_scan(uid, f"✅ Scan completed for {target}")
    with open(f"{data_dir_internal}/scan_summary.txt", "w") as f:
        f.write(f"Scan completed for {target}\n")
        f.write(f"Category: {category}\n")
        f.write(f"UID: {uid}\n")

    return uid

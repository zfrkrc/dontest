# backend/engine.py
import uuid, subprocess, pathlib, json

SCAN_ROOT = pathlib.Path("/app/reports")

def run_scan(ip: str, category: str) -> str:
    uid = uuid.uuid4().hex
    base = SCAN_ROOT / uid
    base.mkdir(parents=True, exist_ok=True)
    data_vol = base / "data"
    data_vol.mkdir(exist_ok=True)

    compose = f"/app/compose/docker-compose.{category}.yml"
    subprocess.run([
        "docker", "compose", "-f", compose,
        "run", "--rm",
        "-e", f"TARGET={ip}",
        "-v", f"{data_vol.absolute()}:/data",
        "merge"
    ], check=True)
    return uid

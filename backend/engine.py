import subprocess
import uuid
import os

BASE_DIR = "/app"
COMPOSE_FILE = f"{BASE_DIR}/compose/docker-compose.string.yml"
REPORT_DIR = f"{BASE_DIR}/reports"


def run_scan(target: str, category: str) -> str:
    uid = uuid.uuid4().hex
    data_dir = f"{REPORT_DIR}/{uid}/data"

    os.makedirs(data_dir, exist_ok=True)

    cmd = [
        "docker", "compose",
        "-f", COMPOSE_FILE,
        "run", "--rm",
        "-e", f"TARGET={target}",
        "-e", f"DATA_DIR={data_dir}",
        "merge"
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Scan failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )

    return uid

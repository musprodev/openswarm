# FastAPI entry point — run with: python server.py

import logging

from agency_swarm.integrations.fastapi import run_fastapi
from dotenv import load_dotenv

from swarm import create_agency

load_dotenv()

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    run_fastapi(
        agencies={
            # you must export your create agency function here
            "open-swarm": create_agency,
        },
        port=8080,
        enable_logging=True,
        allowed_local_file_dirs=[
            "./uploads",
        ],
    )

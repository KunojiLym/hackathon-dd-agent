"""Frontend configuration (env vars)."""

import os
from functools import lru_cache

from env_shared import load_shared_env

load_shared_env()


@lru_cache
def get_frontend_settings() -> dict:
    return {
        "backend_url": os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/"),
        "use_mock_data": os.getenv("USE_MOCK_DATA", "false").lower() in ("1", "true", "yes"),
        "poll_interval_seconds": float(os.getenv("POLL_INTERVAL_SECONDS", "5")),
        "poll_timeout_seconds": float(os.getenv("POLL_TIMEOUT_SECONDS", "300")),
    }

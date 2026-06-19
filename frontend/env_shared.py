from pathlib import Path

from dotenv import load_dotenv

_REPO_ROOT = Path(__file__).resolve().parents[1]
_ROOT_ENV_FILE = _REPO_ROOT / ".env"
_BACKEND_ENV_FILE = _REPO_ROOT / "backend" / ".env"


def load_shared_env() -> None:
    # Match backend/config.py: root .env first, then backend/.env overrides.
    if _ROOT_ENV_FILE.exists():
        load_dotenv(_ROOT_ENV_FILE, override=False)
    if _BACKEND_ENV_FILE.exists():
        load_dotenv(_BACKEND_ENV_FILE, override=True)

from pathlib import Path

from dotenv import load_dotenv

_SHARED_ENV_FILE = Path(__file__).resolve().parents[1] / "backend" / ".env"


def load_shared_env() -> None:
    load_dotenv(_SHARED_ENV_FILE)

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]


def load_env_file() -> None:
    env_path = BASE_DIR / ".env"

    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env_file()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://cake_house_user:cake_house_password@localhost:5432/cake_house_db",
)
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key-in-production")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))

ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

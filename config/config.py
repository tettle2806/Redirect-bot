from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

load_dotenv()

DB_URL = os.getenv("DB_URL")


class DbSettings(BaseSettings):
    url: str = DB_URL
    echo: bool = True


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = f"sqlite+aiosqlite:///db.sqlite3"
    db_echo: bool = False
    # db_echo: bool = True


settings = Setting()

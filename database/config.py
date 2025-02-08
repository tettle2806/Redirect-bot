from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os


load_dotenv()

DB_URL = os.getenv("DB_URL")


class DbSettings(BaseSettings):
    url: str = DB_URL
    echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()


settings = Settings()

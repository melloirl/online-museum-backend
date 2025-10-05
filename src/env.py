import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Literal


def select_env_file() -> str:
    load_dotenv()
    environment = os.getenv("ENV", None)
    if not environment:
        raise ValueError("Missing environment setting")

    return f".env.{environment.lower().strip()}"


env_file = select_env_file()


class Settings(BaseSettings):
    # Environment
    env: Literal["DEV", "STG", "PROD"]

    # CORS
    allowed_origins: str

    # Database Configuration
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int
    postgres_pool_mode: str

    # Storage configuration
    s3_access_key_id: str
    s3_secret_access_key: str
    s3_bucket_name: str
    s3_endpoint_url: str
    s3_base_url: str

    class Config:
        env_file = env_file
        env_file_encoding = "utf-8"

    @property
    def allowed_origins_list(self) -> list[str]:
        if self.env == "DEV" and self.allowed_origins == "*":
            return ["*"]
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}@"
            f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache()
def get_settings() -> Settings:
    return Settings()

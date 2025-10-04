from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Literal


class Settings(BaseSettings):
    # Environment
    env: Literal["DEV", "STG", "PROD"] = "DEV"

    # CORS
    allowed_origins: str = "*"

    # Database Configuration
    postgres_user: str = "museum_user"
    postgres_password: str = "museum_password"
    postgres_db: str = "online_museum"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    class Config:
        env_file = ".env"
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

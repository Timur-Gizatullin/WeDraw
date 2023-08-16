"""For core settings from ENV."""

import functools
import pathlib

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Project settings."""

    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
    ENVIRONMENT: str = "local"

    CORS_ALLOW_ORIGIN_LIST: str = "http://localhost:8000"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "we_draw"
    POSTGRES_PASSWORD: str = "we_draw"
    POSTGRES_DB: str = "we_draw"

    REDIS_DSN: str = "redis://localhost:6379"

    S3_DSN: str = "http://localhost:9000"
    S3_ACCESS_KEY_ID: str = "we_draw"
    S3_SECRET_ACCESS_KEY: str = "we_draw"
    S3_REGION_NAME: str = "eu-central-1"
    S3_BUCKET_NAME: str = "we_draw"

    PRESIGNED_FILE_URL_EXPIRATION_TIME: int = 3600

    AVAILABLE_AVATAR_TYPES: str = "image/jpeg&image/png"
    available_avatar_types: list[str] = AVAILABLE_AVATAR_TYPES.split("&")
    STORAGE_FILE_PATH: str = "media"

    @property
    def cors_allow_origins(self) -> list[str]:
        return self.CORS_ALLOW_ORIGIN_LIST.split("&")

    @property
    def postgres_dsn(self) -> str:
        database = self.POSTGRES_DB if self.ENVIRONMENT != "test" else f"{self.POSTGRES_DB}_test"
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{database}"
        )


@functools.lru_cache
def settings() -> Settings:
    return Settings()

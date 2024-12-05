from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Механизм для управления настройками приложения"""

    POSTGRES_HOST: str = Field(default="localhost")
    POSTGRES_PORT: int = Field(default=5432)
    POSTGRES_DB: str = Field(default="docker")
    POSTGRES_USER: str = Field(default="docker")
    POSTGRES_PASSWORD: str = Field(default="docker")


@lru_cache
def get_settings() -> Settings:
    return Settings()

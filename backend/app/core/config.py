# backend/app/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "GenAI Knowledge Assistant"

    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

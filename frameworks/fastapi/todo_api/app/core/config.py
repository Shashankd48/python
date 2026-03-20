# app/core/config.py
from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    APP_NAME: str = "todo-api"
    MONGO_URI: AnyUrl = "mongodb://localhost:27017"
    MONGO_DB: str = "todo_db"
    # Gunicorn workers count via env etc.

    class Config:
        env_file = ".env"

settings = Settings()

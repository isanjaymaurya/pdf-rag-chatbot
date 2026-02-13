from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "PDF RAG Chatbot"
    DEBUG: bool = True

    # openai
    OPENAI_API_KEY: str
    MODEL_NAME: str

    # redis / celery
    REDIS_URL: str

    # database
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str 

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
        
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

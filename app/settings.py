import os
from functools import lru_cache
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    debug_mode: bool = os.getenv("DEBUG_MODE", "true")

    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        os.getenv("FRONTEND_URL", ""),
    ]

    device: str = os.getenv("DEVICE", "cuda" if os.path.exists("/dev/nvidia0") else "cpu")

    ollama_url: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.2")


@lru_cache
def get_settings() -> Settings:
    return Settings()

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: str = "gemini"  # gemini | groq | ollama | fake
    llm_model: str = "gemini-2.0-flash"
    ollama_base_url: str = "http://localhost:11434"
    google_api_key: str = ""
    groq_api_key: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    app_env:str
    debug:bool
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    
# lru_cache ensures the settings are loaded only once.
@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()

settings = Settings()


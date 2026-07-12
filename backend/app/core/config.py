from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from .env
    """

    # Gemini
    GEMINI_API_KEY: str
    MODEL_NAME: str

    # Embedding Model
    EMBEDDING_MODEL: str

    # ChromaDB
    CHROMA_DB_PATH: str
    CHROMA_COLLECTION: str

    # Upload Folder
    UPLOAD_DIR: str

    # Chunking
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Load settings only once.
    """
    return Settings()


settings = get_settings()
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./erp.db"
    CORS_ORIGINS: str = ""  # comma-separated allowed origins for Render
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"
        env_ignore_empty = True  # blank env vars fall back to defaults


settings = Settings()

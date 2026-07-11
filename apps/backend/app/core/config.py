import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Demand Planning ERP Engine"
    API_V1_STR: str = "/api/v1"
    
    # Render or Neon provides DATABASE_URL in production. 
    # Fallback to local sqlite file inside apps/backend for zero-setup local dev.
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./sql_app.db"
    )

    class Config:
        case_sensitive = True

settings = Settings()
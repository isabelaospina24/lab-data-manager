import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///./app.db"
    
    # API
    api_title: str = "Lab Data Manager API"
    api_version: str = "1.0.0"
    api_description: str = "API para gestionar datos de investigacion cientifica universitaria"
    
    # CORS
    allowed_origins: list = ["http://localhost:5173", "http://localhost:3000"]
    
    # Statistical Analysis
    alpha_significance: float = 0.05
    outlier_threshold: float = 3.0
    
    class Config:
        env_file = ".env"

settings = Settings()

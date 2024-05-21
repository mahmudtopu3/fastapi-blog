import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/blogdb")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

settings = Settings()

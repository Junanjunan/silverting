from pydantic_settings import BaseSettings

from local_settings import *


class Settings(BaseSettings):
    DATABASE_URL: str = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    CURRENT_DB_ENGINE: str = DB_ENGINE


settings = Settings()

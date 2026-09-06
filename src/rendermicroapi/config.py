
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    RENDER_API_KEY : str =""
    RENDER_LIMIT : str =""
    RENDER_API_URL : str =""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

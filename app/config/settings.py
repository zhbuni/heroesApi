from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_URL: str
    DOTABUFF_LINK: str

    model_config = SettingsConfigDict(env_file=".env")
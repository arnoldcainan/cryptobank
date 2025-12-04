from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cryptobank API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "segredo_padrao_apenas_para_desenvolvimento_123"

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
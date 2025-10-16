from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Employee API"
    app_env: str = "development"
    port: int = 8000
    log_level: str = "INFO"

    # Uvicorn settings
    uvicorn_reload: bool = False
    uvicorn_workers: int = 1

    # Security settings
    secret_key: str = "changeme-in-prod"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

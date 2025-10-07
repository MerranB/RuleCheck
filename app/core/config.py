from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "dev"
    app_version: str = "1.0.0"
    app_name: str = "RuleCheck"
    log_level: str = "INFO"
    debug: bool = False

    database_url: str

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "dev"
    app_version: str = "1.0.0"
    app_name: str = "RuleCheck"
    log_level: str = "INFO"
    debug: bool = False
    db_user: str
    db_password: str
    db_name: str

    database_url: str

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

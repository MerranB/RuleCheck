import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_env: str = "dev"
    app_version: str = "1.0.0"
    app_name: str = "RuleCheck"

    debug: bool = False

    db_user: str
    db_password: str
    db_name: str
    db_host: str = "localhost"
    db_port: int = 5432

    @property
    def database_url(self) -> str:

        return (
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:

        env_file = f".env"
        case_sensitive = False


settings = Settings()

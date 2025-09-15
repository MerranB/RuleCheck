import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_env: str = "dev"

    db_user: str
    db_password: str
    db_name: str
    db_host: str = "localhost"
    db_port: int = 5432

    app_name: str = "RuleCheck"
    debug: bool = False

    @property
    def database_url(self) -> str:

        return (
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:

        env_file = f".env.{os.getenv('APP_ENV', 'dev')}"
        case_sensitive = False


# Singleton instance used across app
settings = Settings()

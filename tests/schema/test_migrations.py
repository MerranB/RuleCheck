import pytest
from alembic.config import Config
from alembic import autogenerate, runtime
from sqlalchemy import create_engine
from app.core.config import settings
import app.db.models  # noqa: F401
from app.db.base import Base


@pytest.mark.migration
def test_alembic_migrations_are_in_sync():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", settings.database_url)

    engine = create_engine(settings.database_url)

    try:
        with engine.connect() as connection:
            context = runtime.migration.MigrationContext.configure(connection)
            diff = autogenerate.compare_metadata(context, Base.metadata)

        if diff:
            pytest.fail(
                "Uncommitted migrations detected!\n"
                f"Details: {diff}\n"
                "Run: alembic revision --autogenerate -m '...' and commit the migration."
            )
    finally:
        engine.dispose()

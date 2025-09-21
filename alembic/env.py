import logging
from alembic import context
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine
from app.core.logging_config import setup_logging
from app.db.database import Base
from app.db import models  # noqa: F401
from app.core.config import settings


setup_logging()
logger = logging.getLogger("rulecheck")


def run_migrations_online():
    logger.info("Starting online migration...")

    try:
        connectable = create_engine(settings.database_url)

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=Base.metadata,
                compare_type=True,
                compare_server_default=True,
            )
            script = ScriptDirectory.from_config(context.config)
            current_head = script.get_current_head()
            logger.debug(f"Running Alembic migration. Head version: {current_head}")

            with context.begin_transaction():
                context.run_migrations()

        logger.info("Finished running migrations.")
    except Exception as e:
        logger.exception("Error during online migration")
        raise e


def run_migrations_offline():
    logger.info("Starting offline migration...")

    try:
        url = settings.database_url
        context.configure(
            url=url,
            target_metadata=Base.metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()

        script = ScriptDirectory.from_config(context.config)
        current_head = script.get_current_head()
        logger.info(f"Offline migration. Head version: {current_head}")
        logger.info("Finished offline migration.")
    except Exception as e:
        logger.exception("Error during offline migration")
        raise e


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

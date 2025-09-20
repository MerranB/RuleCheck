from alembic import context
from sqlalchemy import create_engine

from app.db.database import Base
from app.core.config import settings

def run_migrations_online():
    connectable = create_engine(settings.database_url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )

        with context.begin_transaction():
            context.run_migrations()

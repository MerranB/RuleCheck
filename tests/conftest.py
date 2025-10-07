import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient

from app.main import app
from app.db.database import get_db


@pytest.fixture(scope="session")
def postgres_container():
    """Spin up Postgres for the whole test session."""
    with PostgresContainer("postgres:15") as postgres:
        yield postgres


@pytest.fixture(scope="session")
def migrated_engine(postgres_container):
    """Create engine and apply migrations once for test DB."""
    engine = create_engine(postgres_container.get_connection_url())

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option(
        "sqlalchemy.url", postgres_container.get_connection_url()
    )
    command.upgrade(alembic_cfg, "head")  # Apply migrations here
    inspector = inspect(engine)
    print("Tables in test DB:", inspector.get_table_names())
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(migrated_engine):
    """Provide a clean DB session per test, rolled back afterward."""
    connection = migrated_engine.connect()
    transaction = connection.begin()
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=connection)
    session = session_local()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(db_session):
    """FastAPI client with DB session override."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

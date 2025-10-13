import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.db.database import Base
import app.db.models

from app.main import app
from app.db.database import get_db


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:15") as postgres:
        yield postgres


@pytest.fixture(scope="session")
def migrated_engine(postgres_container):
    db_url = postgres_container.get_connection_url()
    engine = create_engine(db_url)
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    print("✅ Tables in test DB:", inspector.get_table_names())
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(migrated_engine):
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
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

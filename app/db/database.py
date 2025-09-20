from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import OperationalError
from app.core.logging_config import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

Base = declarative_base()

try:
    engine = create_engine(
        settings.database_url,
        echo=False,
        pool_pre_ping=True
    )
    logger.info("Database engine created")

    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    logger.info("Database connection established successfully")

except OperationalError as e:
    logger.error("Database connection failed: %s", e)
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


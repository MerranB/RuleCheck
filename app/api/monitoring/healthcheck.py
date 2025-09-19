from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import SessionLocal
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/healthcheck", tags=["infrastructure"])
def healthcheck(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        logger.info("Health check passed")
        return {
            "status": "ok",
            "database": "connected",
            "environment": settings.app_env,
            "version": settings.app_version,
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "environment": settings.app_env,
            "version": settings.app_version,
            "error": str(e)
        }

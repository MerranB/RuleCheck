from fastapi import APIRouter
from app.core.logging_config import logger

router = APIRouter()

@router.get("/", tags=["decisions"])
def list_rules():
    logger.info("Testing Decisions API call.")
    return {"message": "Decisions endpoint ready"}

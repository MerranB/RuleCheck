from fastapi import APIRouter
from app.core.logging_config import logger

router = APIRouter()

@router.get("/", tags=["rules"])
def list_rules():
    logger.info("Testing Rules API call.")
    return {"message": "Rules endpoint ready"}

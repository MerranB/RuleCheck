from fastapi import APIRouter
from app.core.logging_config import logger

router = APIRouter()

@router.get("/", tags=["policies"])
def list_rules():
    logger.info("Testing Policies API call.")
    return {"message": "Policies endpoint ready"}

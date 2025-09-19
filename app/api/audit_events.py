from fastapi import APIRouter
from app.core.logging_config import logger

router = APIRouter()

@router.get("/", tags=["audit_event"])
def list_rules():
    logger.info("Testing Audit_Event API call.")
    return {"message": "Audit Event endpoint ready"}

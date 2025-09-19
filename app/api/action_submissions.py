from fastapi import APIRouter
from app.core.logging_config import logger

router = APIRouter()

@router.get("/", tags=["action_submissions"])
def list_rules():
    logger.info("Testing Action_Submission API call.")
    return {"message": "Action Submissions endpoint ready"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.logging_config import logger
from app.db.models.decision import Decision
from app.db.database import get_db
from app.utils.admin_check import admin_lock

router = APIRouter()


@router.get("/", tags=["decisions"])
def health_check_decisions():
    logger.info("Testing Decisions API call.")
    return {"message": "Decisions endpoint ready"}


@router.get("/get_decision/{decision_id}", tags=["decisions"])
def retrieve_request(decision_id: int, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    decision = db.query(Decision).filter(Decision.id == decision_id).first()
    if not decision:
        raise HTTPException(
            status_code=404, detail=f"Decision with ID {decision_id} not found"
        )
    return decision

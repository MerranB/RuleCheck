from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.logging_config import logger
from app.db.database import get_db
from app.db.models import AuditEvent
from app.utils.admin_check import admin_lock

router = APIRouter()


@router.get("/", tags=["audit_event"])
def health_check_audit_events():
    logger.info("Testing Audit_Event API call.")
    return {"message": "Audit Event endpoint ready"}


@router.get("/get_audit_event/{audit_event_id}", tags=["audit_event"])
def retrieve_audit_event(audit_event_id: int, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    audit_event = db.query(AuditEvent).filter(AuditEvent.id == audit_event_id).first()
    if not audit_event:
        raise HTTPException(
            status_code=404, detail=f"Audit Event with ID {audit_event_id} not found"
        )
    return audit_event

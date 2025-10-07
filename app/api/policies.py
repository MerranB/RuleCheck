from fastapi import APIRouter, Depends, HTTPException
from requests import Session

from app.core.logging_config import logger
from app.db.database import get_db
from app.db.models import Policy, Rule
from app.schemas.policy.create_policy import PolicyCreate
from app.utils.admin_check import admin_lock

router = APIRouter()


@router.get("/", tags=["policies"])
def health_check_policies():
    logger.info("Testing Policies API call.")
    return {"message": "Policies endpoint ready"}


@router.get("/get_policy/{policy_id}", tags=["policies"])
def get_policy(policy_id: int, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(
            status_code=404, detail=f"Policy with ID {policy_id} not found"
        )
    return policy


@router.post("/create_policy", tags=["policies"])
def create_policy(policy: PolicyCreate, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    db_submission = Policy(**policy.model_dump())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return {"message": "Policy created successfully", "id": db_submission.id}


@router.delete("/delete_policy/{policy_id}", tags=["policies"])
def delete_policy(policy_id, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    policy = db.query(Policy).filter(Policy.id == policy_id).first()

    if not policy:
        raise HTTPException(
            status_code=404, detail=f"Policy with ID {policy_id} not found"
        )
    if db.query(Rule).filter(Rule.policy_id == policy_id).all():
        raise HTTPException(
            status_code=409,
            detail="Please remove all rules from the Policy before deleting the policy",
        )

    db.delete(policy)
    db.commit()
    return {"message": f"Policy with ID {policy_id} deleted successfully"}

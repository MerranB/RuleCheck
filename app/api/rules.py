from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from app.core.logging_config import logger
from app.db.database import get_db
from app.db.models import Rule, Policy
from app.schemas.rule.create_rule import RuleCreate
from app.utils.admin_check import admin_lock

router = APIRouter()


@router.get("/", tags=["rules"])
def health_check_rules():
    logger.info("Testing Rules API call.")
    return {"message": "Rules endpoint ready"}


@router.get("/get_rule/{rule_id}", tags=["rules"])
def get_rule(rule_id: int, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail=f"Rule with ID {rule_id} not found")
    return rule


@router.post("/create_rule", tags=["rules"])
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    db_submission = Rule(**rule.model_dump())

    rule = db.query(Policy).filter(Policy.id == db_submission.policy_id).first()
    if not rule:
        raise HTTPException(
            status_code=422,
            detail="Policy ID " + str(db_submission.policy_id) + " is invalid",
        )

    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return {"message": "Rule created successfully", "id": db_submission.id}


@router.delete("/delete_rule/{rule_id}", tags=["rules"])
def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()

    if not rule:
        raise HTTPException(status_code=404, detail=f"Rule with ID {rule_id} not found")
    db.delete(rule)
    db.commit()
    return {"message": f"Rule with ID {rule_id} deleted successfully"}


@router.put("/edit_rule/{rule_id}", tags=["Rules"])
def edit_rule(rule_id: int, rule_update: RuleCreate, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()

    existing_rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not existing_rule:
        raise HTTPException(
            status_code=404, detail=f"Rule with id {rule_id} not found."
        )

    for key, value in rule_update.model_dump(exclude_unset=True).items():
        setattr(existing_rule, key, value)

    db.commit()
    db.refresh(existing_rule)

    return {"message": "Rule updated successfully", "id": existing_rule.id}

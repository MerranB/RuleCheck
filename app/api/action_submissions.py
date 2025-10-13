from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from app.core.logging_config import logger
from app.db.database import get_db
from app.db.models import ActionSubmission
from app.schemas.action_submission.create_action_submission import ActionSubmissionBase
from app.utils.admin_check import admin_lock

router = APIRouter()


@router.get("/", tags=["action_submissions"])
def health_check_action_submissions():
    logger.info("Testing Action Submissions API call.")
    return {"message": "Action Submissions Event endpoint ready"}


@router.get(
    "/get_action_submission/{action_submission_id}", tags=["action_submissions"]
)
def retrieve_request(action_submission_id: int, db: Session = Depends(get_db)):
    # TODO: Restrict this endpoint to admin only
    # TODO: Add role-based access (RBAC)
    admin_lock()
    action_submission = (
        db.query(ActionSubmission)
        .filter(ActionSubmission.id == action_submission_id)
        .first()
    )
    if not action_submission:
        raise HTTPException(
            status_code=404,
            detail=f"Action Submission with ID {action_submission_id} not found",
        )
    return action_submission


@router.post("/create_action_submission", tags=["action_submissions"])
def decide(submission: ActionSubmissionBase, db: Session = Depends(get_db)):
    db_submission = ActionSubmission(**submission.model_dump())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return {"message": "Action Submission created successfully", "id": db_submission.id}

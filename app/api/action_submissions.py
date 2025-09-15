from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["action_submissions"])
def list_rules():
    return {"message": "Action Submissions endpoint ready"}

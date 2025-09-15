from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["audit_event"])
def list_rules():
    return {"message": "Audit Event endpoint ready"}

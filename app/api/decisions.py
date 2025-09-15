from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["decisions"])
def list_rules():
    return {"message": "Decisions endpoint ready"}

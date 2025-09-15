from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["policies"])
def list_rules():
    return {"message": "Policies endpoint ready"}

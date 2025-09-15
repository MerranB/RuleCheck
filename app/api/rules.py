from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["rules"])
def list_rules():
    return {"message": "Rules endpoint ready"}

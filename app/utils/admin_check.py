import os
from fastapi import HTTPException


def admin_lock():
    if os.getenv("ENV", "local") != "local":
        raise HTTPException(status_code=403, detail="Admin access required")

from pydantic import BaseModel

class AuditEventBase(BaseModel):
    name: str
    description: str | None = None


class AuditEventCreate(AuditEventBase):
    pass

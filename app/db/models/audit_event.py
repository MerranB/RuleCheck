from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(
        Integer, ForeignKey("action_submissions.id", ondelete="CASCADE")
    )
    decision_id = Column(Integer, ForeignKey("decisions.id", ondelete="CASCADE"))
    actor_id = Column(Integer, nullable=True)
    actor_role = Column(String, nullable=False)
    action_type = Column(String, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())

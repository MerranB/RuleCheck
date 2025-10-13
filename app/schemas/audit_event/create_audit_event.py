from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base

audit_events = Table(
    "audit_events",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column(
        "submission_id",
        Integer,
        ForeignKey("action_submissions.id", ondelete="CASCADE"),
    ),
    Column("decision_id", Integer, ForeignKey("decisions.id", ondelete="CASCADE")),
    Column("actor_id", Integer, nullable=True),
    Column("actor_role", String, nullable=False),
    Column("action_type", String, nullable=False),
    Column("timestamp", TIMESTAMP(timezone=True), server_default=func.now()),
)

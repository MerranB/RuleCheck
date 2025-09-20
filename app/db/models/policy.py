from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base

## A high-level document


class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    text = Column(String, nullable=True)
    version = Column(String, nullable=True)
    effective_date = Column(
        DateTime,
    )

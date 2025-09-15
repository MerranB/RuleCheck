from sqlalchemy.orm import declarative_base
from .policy import Policy
from .rule import Rule
from .action_submission import ActionSubmission
from .decision import Decision
from .audit_event import AuditEvent

Base = declarative_base()
import sys
import structlog
import logging

from app.core.config import settings

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"

def setup_logging():
    numeric_level = getattr(logging, settings.log_level, logging.INFO)

    logging.basicConfig(
        format=LOG_FORMAT,
        stream=sys.stdout,
        level=getattr(logging, settings.log_level, logging.INFO),
        force = True
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(numeric_level),
        processors=[
            structlog.processors.JSONRenderer(),
        ]
    )
    return logging.getLogger("rulecheck")

logger = setup_logging()

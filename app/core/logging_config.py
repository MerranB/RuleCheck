import sys
import structlog
import logging

LOG_FORMAT = (
    "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

def setup_logging():
    logging.basicConfig(
        format=LOG_FORMAT,
        stream=sys.stdout,
        level=logging.INFO
    )
    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer()
        ]
    )

logger = logging.getLogger("rulecheck")
import logging

from flask import current_app
from flask_healthz import HealthError

logger = logging.getLogger(__name__)


def check_readiness():
    logging.debug("Check readiness")
    logging.debug("DEBUG=%s", current_app.config["DEBUG"])
    return True


def liveness():
    pass


def readiness():
    try:
        check_readiness()
    except Exception:
        raise HealthError("Readiness checks failed!")

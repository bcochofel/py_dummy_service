from flask_healthz import HealthError


def check_readiness():
    return True


def liveness():
    pass


def readiness():
    try:
        check_readiness()
    except Exception:
        raise HealthError("Readiness checks failed!")

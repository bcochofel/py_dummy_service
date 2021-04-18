# main blueprint
import logging
import socket

from flask import Blueprint, jsonify
from py_dummy_service import __app_name__, __app_version__


logger = logging.getLogger(__name__)
bp = Blueprint("main", __name__)


@bp.route("/")
@bp.route("/index")
@bp.route("/info")
def index():
    """Index route."""
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    except:
        hostname = "unknown"
        ip = "unknown"
    logging.debug("Application name: %s", __app_name__)
    logging.debug("Application version: %s", __app_version__)
    logging.debug("Hostname: %s", hostname)
    logging.debug("IP: %s", ip)
    return jsonify(
        app_name=__app_name__,
        app_version=__app_version__,
        hostname=hostname,
        ip=ip,
    )
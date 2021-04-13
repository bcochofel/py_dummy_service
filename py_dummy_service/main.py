# main blueprint
import logging
import subprocess

from flask import Blueprint, jsonify
from py_dummy_service import __app_name__, __app_version__


logger = logging.getLogger(__name__)
bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Index route."""
    hostname = subprocess.check_output("hostname").decode("utf8").strip()
    logging.debug("Application name: %s", __app_name__)
    logging.debug("Application version: %s", __app_version__)
    logging.debug("Hostname: %s", hostname)
    return jsonify(
        app_name=__app_name__,
        app_version=__app_version__,
        hostname=hostname,
    )
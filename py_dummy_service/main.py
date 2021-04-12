import logging
import subprocess

from flask import Blueprint, jsonify, request
from py_dummy_service import __app_name__, __app_version__


logger = logging.getLogger(__name__)
bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Index route."""
    logging.debug("debug log")
    logging.info("info log")
    logging.warning("warning log")
    logging.error("error log")
    return jsonify(
        app_name=__app_name__,
        app_version=__app_version__,
        hostname=subprocess.check_output("hostname").decode("utf8").strip(),
    )


@bp.route("/headers")
def headers():
    """Show request Headers."""
    logging.debug("headers")
    headers = str(request.headers).split("\r\n")
    stripped_headers = [string for string in headers if string != ""]
    return jsonify(stripped_headers)
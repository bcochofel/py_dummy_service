import logging
import requests
import socket

from flask import Blueprint, current_app, jsonify
from py_dummy_service import __app_name__, __app_version__


logger = logging.getLogger(__name__)
bp = Blueprint("backend", __name__)


@bp.route("/info")
def info():
    """Info."""
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


@bp.route("/status/<status>")
def status_code(status=200):
    """Simulate status codes using backend."""
    logging.info("request status %s from backend", status)
    url = "{host}/api/v1/status/{status}".format(
        host=current_app.config["BACKEND_URL"], status=status
    )
    try:
        r = requests.get(url)
        return r.json(), r.status_code
    except requests.exceptions.RequestException as e:
        logging.error("%s", e)
    return jsonify({"status": "service unavailable"}), 200


@bp.route("/<path:path>")
def generic_path(path):
    """Simulate paths using backend."""
    logging.info("request path %s from backend", path)
    url = "{host}/api/v1/{path}".format(
        host=current_app.config["BACKEND_URL"], path=path
    )
    try:
        r = requests.get(url)
        return r.json(), r.status_code
    except requests.exceptions.RequestException as e:
        logging.error("%s", e)
    return jsonify({"status": "service unavailable"}), 200
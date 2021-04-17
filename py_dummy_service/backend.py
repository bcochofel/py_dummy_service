import logging
import requests

from flask import Blueprint, current_app, jsonify


logger = logging.getLogger(__name__)
bp = Blueprint("backend", __name__)


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
# api blueprint
import logging
from textwrap import wrap

from flask import Blueprint, jsonify, request
from py_dummy_service import __app_name__, __app_version__


logger = logging.getLogger(__name__)
bp = Blueprint("api", __name__)
methods = ["GET", "POST", "PATCH", "DELETE"]


@bp.route("/headers")
def headers():
    """Show request Headers."""
    logging.debug("headers")
    headers = str(request.headers).split("\r\n")
    stripped_headers = [string for string in headers if string != ""]
    return jsonify(stripped_headers)


@bp.route("/<path:path>", methods=methods)
def generic(path):
    logging.info("endpoint: %s", path)
    logging.info("headers: %s", request.headers)
    logging.info("body: %s", request.get_data())
    logging.info("data: %s", request.data.decode())
    logging.info("json: %s", request.get_json())
    logging.info("form: %s", request.form)

    return jsonify(
        {
            "endpoint": path,
            "data": request.data.decode("utf-8"),
            "form": request.form,
            "json": request.get_json(),
        }
    )
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
    logging.info("headers: %s", request.headers)
    return jsonify(dict(request.headers))


@bp.route("/status/<status>", methods=["GET"])
def status_code(status=200):
    """Simulate Status Codes"""
    logging.info("status: %s", status)
    return jsonify({"status": status}), status


@bp.route("/<path:path>", methods=methods)
def generic(path):
    logging.info("endpoint: %s", path)
    logging.info("method: %s", request.method)
    logging.info("headers: %s", request.headers)
    logging.info("cookies: %s", request.cookies)
    logging.info("data: %s", request.data.decode())
    logging.info("json: %s", request.get_json())
    logging.info("args: %s", request.args)
    logging.info("form: %s", request.form)
    logging.info("remote_addr: %s", request.remote_addr)

    return jsonify(
        {
            "endpoint": path,
            "method": request.method,
            "headers": dict(request.headers),
            "cookies": request.cookies,
            "data": request.data.decode("utf-8"),
            "json": request.get_json(),
            "args": request.args,
            "form": request.form,
            "remote_addr": request.remote_addr,
        }
    )

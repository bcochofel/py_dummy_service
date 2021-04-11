import logging

from flask import Blueprint, jsonify


logger = logging.getLogger(__name__)
bp = Blueprint("errors", __name__)


@bp.app_errorhandler(404)
def handle_404(err):
    logging.debug("404")
    logging.error("%s", err)
    return jsonify(error=str(err)), 404


@bp.app_errorhandler(500)
def handle_500(err):
    logging.debug("500")
    logging.error("%s", err)
    return jsonify(error=str(err)), 500
from flask import Blueprint, jsonify


bp = Blueprint("errors", __name__)


@bp.app_errorhandler(404)
def handle_404(err):
    return jsonify(error=str(err)), 404


@bp.app_errorhandler(500)
def handle_500(err):
    return jsonify(error=str(err)), 500
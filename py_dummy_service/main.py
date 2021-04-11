from flask import Blueprint, jsonify
from py_dummy_service import __app_name__, __app_version__


bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """
    Index route
    """
    return jsonify(app_name=__app_name__, app_version=__app_version__)

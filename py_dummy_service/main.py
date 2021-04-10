from flask import Blueprint


bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """
    Index route
    """
    return "Index"

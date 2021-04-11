# __init__.py

# base imports
import os

# third party imports
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics


# local imports
from config import config


__app_name__ = "py-dummy-service"
__app_version__ = "0.2.0"

metrics = PrometheusMetrics.for_app_factory()
metrics.info("app_info", "Dummy Service", version=__app_version__)


def create_app(conf_name=None):
    """
    Create and Configure the app

    Args:
        conf_name (str): configuration environment
    """
    app = Flask(__name__, instance_relative_config=True)

    # load config
    if conf_name is None:
        config_name = os.getenv("FLASK_ENV", "default")
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config[conf_name])

    # prometheus exporter
    metrics.init_app(app)

    # import blueprints
    from py_dummy_service import main
    from py_dummy_service import errors

    app.register_blueprint(main.bp)
    app.register_blueprint(errors.bp)
    app.add_url_rule("/", endpoint="index")

    return app

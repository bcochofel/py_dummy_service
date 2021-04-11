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


def create_app():
    """
    Create and Configure the app

    Args:
        config_name (class): configuration environment
    """
    app = Flask(__name__, instance_relative_config=True)

    # load config
    config_name = os.getenv("FLASK_ENV", "default")
    app.config.from_object(config[config_name])

    # prometheus exporter
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version=__app_version__)

    # import blueprints
    from py_dummy_service import main

    app.register_blueprint(main.bp)
    app.add_url_rule("/", endpoint="index")

    return app

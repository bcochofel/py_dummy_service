# __init__.py

# base imports
import logging
from logging.config import dictConfig
from os import getenv

# third party imports
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from flask_healthz import healthz
from jaeger_client import Config
from flask_opentracing import FlaskTracing


# local imports
from config import config


__app_name__ = "py-dummy-service"
__app_version__ = "1.1.1"

metrics = PrometheusMetrics.for_app_factory()
metrics.info("app_info", "Dummy Service", version=__app_version__)


def create_app(config_name=None):
    """
    Create and Configure the app

    Args:
        config_name (str): configuration environment
    """
    app = Flask(__name__, instance_relative_config=True)

    # load config
    if config_name is None:
        config_name = getenv("FLASK_ENV", "default")
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # prometheus exporter config
    metrics.init_app(app)

    # pre and post handlers
    register_pre_request_handlers(app)
    register_post_request_handlers(app)

    # logging config
    setup_logging(app)

    logging.info("Starting Dummy Service")
    # logging.debug("debug log message")
    # logging.info("info log message")
    # logging.warning("warning log message")
    # logging.error("error log message")

    # blueprints config
    register_blueprints(app)

    return app


def register_pre_request_handlers(app):
    pass


def register_post_request_handlers(app):
    pass


def setup_logging(app):
    debug = app.config["DEBUG"]
    log_level = app.config["LOG_LEVEL"]

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] [%(levelname)s] in %(module)s: %(message)s",
                },
                "access": {
                    "format": "%(message)s",
                },
            },
            "handlers": {
                "console": {
                    "level": log_level,
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                },
                "error_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "default",
                    "filename": "/var/log/gunicorn.error.log",
                    "maxBytes": 10000,
                    "backupCount": 10,
                    "delay": "True",
                },
                "access_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "formatter": "access",
                    "filename": "/var/log/gunicorn.access.log",
                    "maxBytes": 10000,
                    "backupCount": 10,
                    "delay": "True",
                },
            },
            "loggers": {
                "gunicorn.error": {
                    "handlers": ["console"] if debug else ["console", "error_file"],
                    "level": log_level,
                    "propagate": False,
                },
                "gunicorn.access": {
                    "handlers": ["console"] if debug else ["console", "access_file"],
                    "level": log_level,
                    "propagate": False,
                },
            },
            "root": {
                "level": "DEBUG" if debug else "INFO",
                "handlers": ["console"] if debug else ["console"],
            },
        }
    )


def register_blueprints(app):
    """Blueprints register."""
    from py_dummy_service import main
    from py_dummy_service import api
    from py_dummy_service import errors

    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp, url_prefix="/api/v1")
    app.register_blueprint(errors.bp)
    app.register_blueprint(healthz, url_prefix="/healthz")
    app.add_url_rule("/", endpoint="index")

# configuration file

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Common configuration for all environments
    """

    # insert here common config

    # flask healthz config
    HEALTHZ = {
        "live": "py_dummy_service.healthz.liveness",
        "ready": "py_dummy_service.healthz.readiness",
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    DEBUG_METRICS = 1
    LOG_LEVEL = "DEBUG"


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    DEBUG_METRICS = 0
    LOG_LEVEL = "INFO"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DEBUG_METRICS = 0
    LOG_LEVEL = "INFO"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": ProductionConfig,
}

# configuration file

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Common configuration for all environments
    """

    # insert here common config


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    DEBUG_METRICS = 1


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    DEBUG_METRICS = 0


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DEBUG_METRICS = 0


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": ProductionConfig,
}

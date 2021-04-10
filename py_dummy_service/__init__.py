# __init__.py
import os
from flask import Flask


def create_app():
    """
    Create and Configure the app
    """
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # import blueprints
    from py_dummy_service import main

    app.register_blueprint(main.bp)
    app.add_url_rule("/", endpoint="index")

    return app

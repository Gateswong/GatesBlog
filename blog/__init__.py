from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint)

    return app

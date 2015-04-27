from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "control_panel.login"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint)

    from .control_panel import control_panel as control_panel_blueprint
    app.register_blueprint(control_panel_blueprint)

    return app


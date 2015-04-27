from flask import Blueprint

control_panel = Blueprint("control_panel", __name__)

from . import routes

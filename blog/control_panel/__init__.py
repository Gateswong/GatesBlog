from flask import Blueprint, url_for, redirect

control_panel = Blueprint("control_panel", __name__)

from ..utils import need_setup
from . import routes


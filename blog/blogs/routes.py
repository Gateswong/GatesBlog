from flask import render_template
from . import blogs


@blogs.route("/")
def home():
    return render_template("blogs/index.html")

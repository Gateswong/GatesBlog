from flask import render_template
from . import blogs


@blogs.route("/")
def home():
    return render_template("blogs/index.html",
                           site={"Title": "My Blog", "Brand": "My Blog"})

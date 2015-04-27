from flask import (render_template,
                   current_app,
                   request,
                   redirect,
                   url_for
                   )

from ..models import (Setting,
                      SETTING_BLOG_NAME
                      )

from . import control_panel
from .forms import SetupForm
from .utils import need_setup


@control_panel.route("/setup", methods=["GET", "POST"])
def setup():
    if not need_setup():
        return render_template("control_panel/message_page.html",
                               message="You site is already setup, you don't need to do it again.",
                               title="Site already setup",
                               next_url=url_for("blogs.home"))
    form = SetupForm()
    if form.validate_on_submit():
        if Setting.apply_setting(SETTING_BLOG_NAME, form.blog_name.data):
            return redirect(url_for("control_panel.setup_success"))
    return render_template("control_panel/setup.html", form=form)


@control_panel.route("/setup/success", methods=["GET"])
def setup_success():
    return render_template("control_panel/message_page.html",
                           message="Now the blog is setup!",
                           title="Setup complete!",
                           next_url=url_for("blogs.home"))


@control_panel.route("/login")
def login():
    return render_template("control_panel/login.html")



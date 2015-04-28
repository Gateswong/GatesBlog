from flask import (render_template,
                   redirect,
                   url_for,
                   flash,
                   request
                   )
from flask.ext.login import (login_user,
                             logout_user,
                             login_required
                             )

from ..models import (Setting,
                      User,
                      SETTING_BLOG_NAME
                      )
from ..utils import (load_page_meta,
                     need_setup
                     )

from . import control_panel
from .forms import (SetupForm,
                    LoginForm
                    )


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


@control_panel.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Invalid email or password.")
            return redirect(url_for(".login"))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get("next") or url_for("blogs.home"))
    page_meta = load_page_meta(title_prefix="Login")
    return render_template("control_panel/login.html",
                           form=form,
                           page_meta=page_meta)


@control_panel.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(request.args.get("next") or url_for("blogs.home"))

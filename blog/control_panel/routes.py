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

from ..models import (User,
                      Post,
                      )

from . import control_panel
from .forms import (SetupForm,
                    LoginForm,
                    NewPostForm
                    )


@control_panel.route("/cpanel")
@login_required
def index():
    posts = Post.query_page_of_posts()
    return render_template("control_panel/index.html",
                           posts=posts,
                           page_num=1,
                           page_total=Post.total_pages(),
                           )


@control_panel.route("/cpanel/posts")
@login_required
def post_list():
    # Get Page Num from query string
    try:
        page_num = int(request.args.get("page", 1))
    except ValueError:
        page_num = 1

    # Get tags and category filter
    tags = request.args.get("tags", None)
    if tags: tags = tags.split(",")
    category = request.args.get("category", "")

    posts = Post.query_page_of_posts(skip=(page_num - 1) * 25,
                                     limit=25,
                                     tags=tags,
                                     category=category)

    return render_template("control_panel/index.html",
                           posts=posts,
                           page_num=page_num,
                           page_total=Post.total_pages())


@control_panel.route("/cpanel/newpost", methods=["GET", "POST"])
@login_required
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.body.data
        Post.new_post(title=title, content=content)
        return redirect(url_for("control_panel.index"))
    return render_template("control_panel/new_post.html",
                           form=form)

@control_panel.route("/cpanel/editpost", methods=["GET", "POST"])
@login_required
def edit_post():
    return "Not implemented"


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
    return render_template("control_panel/login.html",
                           form=form
                           )


@control_panel.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(request.args.get("next") or url_for("blogs.home"))


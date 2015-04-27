from flask import (render_template,
                   redirect,
                   url_for
                   )

from . import blogs
from .utils import load_page_meta
from ..control_panel.utils import NotSetup
from ..models import (Setting,
                      SETTING_BLOG_NAME
                      )


@blogs.route("/")
def home():
    try:
        page_meta = load_page_meta()
    except NotSetup:
        return redirect(url_for("control_panel.setup"))
    return render_template("blogs/index.html",
                           page_meta=page_meta)
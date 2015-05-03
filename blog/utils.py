from flask import redirect, url_for
from sqlalchemy.orm.exc import NoResultFound

from functools import wraps

from . import db
from .models import (Setting,
                     SETTING_BLOG_NAME
                     )


def load_page_meta(title_prefix=None):
    ds = Setting.load_settings([SETTING_BLOG_NAME])

    if SETTING_BLOG_NAME not in ds:
        raise NotSetup

    page_meta = {
        "Title": ds[SETTING_BLOG_NAME][0] if title_prefix is None else
        "%s | %s" % (title_prefix, ds[SETTING_BLOG_NAME][0]),
        "Brand": ds[SETTING_BLOG_NAME][0]
    }

    return page_meta


class NotSetup(Exception):
    pass


def need_setup():
    try:
        db.session.query(Setting).filter(Setting.id == SETTING_BLOG_NAME).one()
        return False
    except NoResultFound:
        return True


def setup_required(func):
    """
    If you decorate a view with this, it will ensure that the blog is setup
    before calling the view.

    Similar to the login_required in flask-Login
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if need_setup():
            return redirect(url_for("control_panel.setup"))
        return func(*args, **kwargs)
    return decorated_view





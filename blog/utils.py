from sqlalchemy.orm.exc import NoResultFound

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


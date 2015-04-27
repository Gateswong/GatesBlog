from sqlalchemy.orm.exc import NoResultFound

from .. import db
from ..models.setting import (Setting,
                              SETTING_BLOG_NAME
                              )


class NotSetup(Exception):
    pass


def need_setup():
    try:
        db.session.query(Setting).filter(Setting.id == SETTING_BLOG_NAME).one()
        return False
    except NoResultFound:
        return True


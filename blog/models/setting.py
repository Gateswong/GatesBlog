from sqlalchemy.orm.exc import NoResultFound

from .. import db

SETTING_BLOG_NAME = 1


class Setting(db.Model):
    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text(), nullable=False)
    extra = db.Column(db.Text())

    @classmethod
    def apply_setting(cls, id, value=None, extra=None):
        try:
            setting = db.session.query(Setting).filter(Setting.id == id).one()
            setting.value = value
            setting.extra = extra
        except NoResultFound:
            setting = Setting(id=id, value=value, extra=extra)
            db.session.add(setting)

        db.session.commit()
        return True

    @classmethod
    def load_settings(cls, id_list):
        settings = db.session.query(Setting).filter(Setting.id.in_(id_list)).all()
        return dict([(s.id, (s.value, s.extra)) for s in settings])


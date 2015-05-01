from arrow import arrow

from .. import db


__all__ = ["Post"]


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)

    time_created = db.Column(db.DateTime, default=arrow.Arrow.now().datetime)
    time_modified = db.Column(db.DateTime, default=arrow.Arrow.now().datetime)


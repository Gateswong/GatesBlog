from arrow import arrow
from datetime import datetime
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from .. import db


__all__ = ["User"]


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(64))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


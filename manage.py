#!/usr/bin/env python
import os

from blog import create_app

from flask.ext.script import Manager


app = create_app(os.getenv("FLASK_CONFIG") or "default")
manager = Manager(app)


@manager.command
def init_database():
    from blog import db
    from blog import models

    db.create_all()


@manager.command
def recreate_database():
    from blog import db
    from blog import models

    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()


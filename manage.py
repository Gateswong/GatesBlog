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

    db.reflect()  # hacky solution
                  # ref: http://jrheard.tumblr.com/post/12759432733/dropping-all-tables-on-postgres-using
    db.drop_all()
    db.create_all()


@manager.command
def adduser(email, username):
    """Regist a new user"""
    from getpass import getpass
    password = getpass()
    password2 = getpass()
    if password != password2:
        import sys
        sys.exit("Create user failed: passwords do not match!")

    from blog import db
    from blog.models.user import User

    db.create_all()
    user = User(email=email, username=username, password=password, name=username)
    db.session.add(user)
    db.session.commit()

    print("Create user success: {0}".format(username))


if __name__ == "__main__":
    manager.run()


import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    BLOG_NAME = u"Your Blog Name"
    NAV_ITEMS = [
        {"name": "Github", "link": "http://github.com/Gateswong", "new_window": True},
        {"name": "Bitbucket", "link": "http://bitbucket.org/Gatesice"},
    ]


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("BLOG_DATABASE_URL") or \
        "postgresql://localhost/blog"
    WTF_CSRF_SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY")
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "s3cr3t"
    SQLALCHEMY_DATABASE_URI = os.environ.get("BLOG_DATABASE_URL") or \
        "postgresql://localhost/blog_dev"
    WTF_CSRF_SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY") or \
        "csrf_s3cr3t"

    SUB_MARK = "dev"


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "s3cr3t"
    SQLALCHEMY_DATABASE_URI = os.environ.get("BLOG_DATABASE_URL") or \
        "postgresql://localhost/blog_test"
    WTF_CSRF_SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY") or \
        "csrf_s3cr3t"

    SUB_MARK = "test"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}

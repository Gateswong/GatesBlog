import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")


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


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "s3cr3t"
    SQLALCHEMY_DATABASE_URI = os.environ.get("BLOG_DATABASE_URL") or \
        "postgresql://localhost/blog_test"
    WTF_CSRF_SECRET_KEY = os.environ.get("WTF_CSRF_SECRET_KEY") or \
        "csrf_s3cr3t"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}

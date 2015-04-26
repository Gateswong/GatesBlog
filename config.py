import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "s3cr3t"


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = "s3cr3t"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}

class Config(object):
    pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production_user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development_user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing_user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

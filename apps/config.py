class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductConfig(Config):
    pass


config_map = {
    'dev': DevelopmentConfig,
    'prod': ProductConfig,
}
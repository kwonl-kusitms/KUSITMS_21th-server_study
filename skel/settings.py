class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JWT_SECRET_KEY = "super-duper-seceret"

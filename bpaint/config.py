from flask_uploads import IMAGES


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bpaint.sqlite'
    SECRET_KEY = 'dev'
    ALLOWED_FILES = IMAGES

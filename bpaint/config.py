import os

from flask_uploads import IMAGES

MEDIUM_CHOICES = [
        ('OA', 'Oil/Acrylic'),
        # ('WC', 'Watercolor'),
        # ('DR', 'Digital (RGB)'),
        # ('DC', 'Digital (CMYK)'),
        # ('DH', 'Digital (HSL)'),
        ]

DEFAULT_PIC_SEARCH_THRESHOLD = 30
DEFAULT_PIC_SEARCH_NUM_COLORS = 5


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bpaint.sqlite'
    SECRET_KEY = 'dev'
    ALLOWED_FILES = IMAGES
    UPLOAD_FOLDER = os.path.abspath('./bpaint/static/images')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_ECHO = True

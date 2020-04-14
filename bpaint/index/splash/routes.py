from flask import Blueprint


bp = Blueprint('splash', __name__)


@bp.route('/')
def splash():
    return __name__

from flask import Blueprint


bp = Blueprint('index', __name__)


@bp.route('/index')
def index():
    return __name__

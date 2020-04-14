from flask import Blueprint


bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/')
def search():
    return __name__

@bp.route('/image')
def image_search():
    return __name__

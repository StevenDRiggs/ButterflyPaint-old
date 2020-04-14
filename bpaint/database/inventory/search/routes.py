from flask import Blueprint


bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/')
def search():
	pass

@bp.route('/image')
def image_search():
	pass
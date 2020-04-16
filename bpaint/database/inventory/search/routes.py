from flask import Blueprint, render_template


bp = Blueprint('search', __name__, url_prefix='/search', template_folder='templates')


@bp.route('/')
def search():
    return render_template('search/search.html')

@bp.route('/image')
def image_search():
    return render_template('search/image.html')

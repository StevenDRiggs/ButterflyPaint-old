from flask import Blueprint, render_template

bp = Blueprint('pic_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/pic')


@bp.route('/')
def pic_search():
    return render_template('pic/index.html')

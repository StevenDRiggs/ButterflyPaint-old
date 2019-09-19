from flask import Blueprint, render_template

bp = Blueprint('text_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/text')


@bp.route('/')
def text_search():
    return render_template('text/index.html')

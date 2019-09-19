from flask import Blueprint, redirect, render_template, url_for

bp = Blueprint('pic_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/pic')


@bp.route('/')
def pic_search():
    return render_template('pic/index.html')

@bp.route('/results')
def pic_search_results():
    return redirect(url_for('search.results'))

from flask import Blueprint, redirect, render_template, url_for

bp = Blueprint('text_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/text')


@bp.route('/')
def text_search():
    return render_template('text/index.html')

@bp.route('/results')
def text_search_results():
    return redirect(url_for('search.results'))

from flask import Blueprint, redirect, render_template, url_for

bp = Blueprint('text_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/text')


@bp.route('/')
def text_search():
    from bpaint import db
    colors = {color.name: color.swatch for color in db.session.execute('select name, swatch from color').fetchall()}
    return render_template('text/index.html', colors=colors)

@bp.route('/results')
def text_search_results():
    return redirect(url_for('search.results'))

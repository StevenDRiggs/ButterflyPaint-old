from flask import Blueprint, redirect, render_template, url_for

bp = Blueprint('text_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/text')


@bp.route('/')
def text_search():
    from bpaint import Color

    display_info = {color.id: {
        'name': color.name,
        'swatch': color.swatch,
        'used_in': [c.name for c in color.used_in],
    } for color in Color.query.all()}

    return render_template('text/index.html', display_info=display_info)

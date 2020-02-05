from flask import Blueprint, render_template


bp = Blueprint('details', __name__, static_folder='static', template_folder='templates', url_prefix='/details')


@bp.route('/<int:rec_id>')
def details(rec_id):
    from bpaint import load_db

    rec = load_db(rec_id)[0]

    current = {
            'medium': rec.medium,
            'name': rec.name,
            'pure': rec.pure,
            'swatch': rec.swatch,
            'recipe': rec.recipe,
            'used_in': list(rec.used_in)
            }
    print(f'\n{current=}\n')

    return render_template('details/index.html', current=current)

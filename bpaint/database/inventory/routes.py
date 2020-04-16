from flask import Blueprint, render_template


bp = Blueprint('inventory', __name__, url_prefix='/inventory', template_folder='templates')


@bp.route('/')
def inventory():
    return render_template('inventory/inventory.html')

@bp.route('/details/<int:color_id>')
def individual_color_detail(color_id):
    return render_template('inventory/details_color_id.html')

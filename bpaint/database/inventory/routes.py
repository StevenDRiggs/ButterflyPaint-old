from flask import Blueprint


bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/')
def inventory():
    return __name__

@bp.route('/details/<int:color_id>')
def individual_color_detail(color_id):
    return __name__

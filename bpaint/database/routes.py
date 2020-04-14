from flask import Blueprint


bp = Blueprint('database', __name__, url_prefix='/database')


@bp.route('/')
def database():
    return __name__


@bp.route('/add')
def add_to_database():
    return __name__

@bp.route('/add/single')
def add_single_color_to_database():
    return __name__

@bp.route('/add/batch')
def batch_add_colors_to_database():
    return __name__


@bp.route('/update')
def update_database():
    return __name__

@bp.route('/update/single')
def update_single_color():
    return __name__

@bp.route('/update/single/<int:color_id>')
def update_single_color_with_color_id(color_id):
    return __name__

@bp.route('/update/batch')
def batch_update_colors():
    return __name__

@bp.route('/update/batch/update')
def batch_update_colors_with_choices(choices):
    return __name__


@bp.route('delete')
def delete_from_database():
    return __name__

@bp.route('/delete/single')
def delete_single_color():
    return __name__

@bp.route('/delete/batch')
def batch_delete_colors():
    return __name__


@bp.route('verify')
def verify_changes(changes):
    return __name__

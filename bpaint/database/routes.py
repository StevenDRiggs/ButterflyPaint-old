from flask import Blueprint


bp = Blueprint('database', __name__, url_prefix='/database')


@bp.route('/')
def database():
	pass


@bp.route('/add')
def add_to_database():
	pass

@bp.route('/add/single')
def add_single_color_to_database():
	pass

@bp.route('/add/batch')
def batch_add_colors_to_database():
	pass


@bp.route('/update')
def update_database():
	pass

@bp.route('/update/single')
def update_single_color():
	pass

@bp.route('/update/single/<int:color_id>')
def update_single_color_with_color_id(color_id):
	pass

@bp.route('/update/batch')
def batch_update_colors():
	pass

@bp.route('/update/batch/update')
def batch_update_colors_with_choices(choices):
	pass


@bp.route('delete')
def delete_from_database():
	pass

@bp.route('/delete/single')
def delete_single_color():
	pass

@bp.route('/delete/batch')
def batch_delete_colors():
	pass


@bp.route('verify')
def verify_changes(changes):
	pass

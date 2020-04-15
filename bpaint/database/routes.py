from flask import Blueprint, render_template


bp = Blueprint('database', __name__, url_prefix='/database', template_folder='templates')


@bp.route('/')
def database():
    return render_template('database/database.html')


@bp.route('/add')
def add_to_database():
    return render_template('database/add.html')

@bp.route('/add/single')
def add_single_color_to_database():
    return render_template('database/add_single.html')

@bp.route('/add/batch')
def batch_add_colors_to_database():
    return render_template('database/add_batch.html')


@bp.route('/update')
def update_database():
    return render_template('database/update.html')

@bp.route('/update/single')
def update_single_color():
    return render_template('database/update_single.html')

@bp.route('/update/single/<int:color_id>')
def update_single_color_with_color_id(color_id):
    return render_template('database/update_single_color_id.html')

@bp.route('/update/batch')
def batch_update_colors():
    return render_template('database/update_batch.html')

@bp.route('/update/batch/update')
def batch_update_colors_with_choices(choices):
    return render_template('database/update_batch_update.html')


@bp.route('delete')
def delete_from_database():
    return render_template('database/delete.html')

@bp.route('/delete/single')
def delete_single_color():
    return __name__

@bp.route('/delete/batch')
def batch_delete_colors():
    return __name__


@bp.route('verify')
def verify_changes(changes):
    return __name__

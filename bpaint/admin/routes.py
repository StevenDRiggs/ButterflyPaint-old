from flask import Blueprint, render_template

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('index.html')


@bp.route('/db/')
def db_home():
    pass

@bp.route('/db/add', methods=['GET', 'POST'])
def db_add():
    pass

@bp.route('/db/update', methods=['GET', 'POST'])
def db_update():
    pass

@bp.route('/db/delete', methods=['GET', 'POST'])
def db_delete():
    pass

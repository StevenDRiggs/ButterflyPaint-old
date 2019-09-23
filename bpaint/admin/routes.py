from flask import Blueprint, render_template

from bpaint.admin.forms import AddToDatabaseForm

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/index.html')


@bp.route('/db/')
def db_home():
    return render_template('admin/db_home.html')

@bp.route('/db/add', methods=['GET', 'POST'])
def db_add():
    form = AddToDatabaseForm()
    if form.validate_on_submit():
        return redirect('splash.index')
    return render_template('admin/db_add.html', form=form)

@bp.route('/db/update', methods=['GET', 'POST'])
def db_update():
    return render_template('admin/db_update.html')

@bp.route('/db/delete', methods=['GET', 'POST'])
def db_delete():
    return render_template('admin/db_delete.html')

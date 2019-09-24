from flask import Blueprint, flash, redirect, render_template, request, url_for

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
    if request.method == 'POST':
        if form.validate_on_submit():
            from bpaint import db
            from bpaint.models import Color
            record = form.data
            record.pop('csrf_token')
            record.pop('submit')
            color = Color(**record)
            db.session.add(color)
            db.session.commit()
            flash('Success!')
            return redirect(url_for('admin.db_add'))
        else:
            return form.errors
    return render_template('admin/db_add.html', form=form)

@bp.route('/db/update', methods=['GET', 'POST'])
def db_update():
    return render_template('admin/db_update.html')

@bp.route('/db/delete', methods=['GET', 'POST'])
def db_delete():
    return render_template('admin/db_delete.html')

@bp.route('/db/<string:next_action>/db_fetch', methods=['GET', 'POST'])
def db_fetch(next_action):
    if request.method == 'POST':
        return request.data
    from bpaint.models import Color
    records_all = Color.query.all()
    return render_template('admin/db_fetch.html', records=records_all, next_action=next_action)
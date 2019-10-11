import os

from flask import Blueprint, flash, redirect, render_template, request, url_for

from werkzeug.utils import secure_filename

from bpaint.admin.forms import AddToDatabaseForm, DeleteForm, UpdateForm

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/index.html')


@bp.route('/db/')
def db_home():
    return render_template('admin/db_home.html')

def load_db():
    from bpaint.models import Color
    records_all = Color.query.all()
    return records_all

@bp.route('/db/add', methods=['GET', 'POST'])
def db_add():
    form = AddToDatabaseForm()
    records = load_db()
    form.recipe.choices = []
    for record in records:
        form.recipe.choices.append((record.id, record.name))
    if not form.recipe.choices:
        del form.recipe
    if request.method == 'POST':
        if form.validate_on_submit():
            from bpaint import app, db, uploads
            from bpaint.models import Color
            formdata = form.data
            image = formdata.pop('swatch')
            image.filename = secure_filename(image.filename)
            image.resize((200, 200))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], image.filename), 'w'):
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            formdata.pop('csrf_token')
            formdata.pop('submit')
            formdata['swatch'] = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            formdata['recipe'] = '|'.join(formdata.get('recipe', []))
            color = Color(**formdata)
            db.session.add(color)
            db.session.commit()
            if not color.recipe:
                color.recipe = str(color.id)
                db.session.add(color)
                db.session.commit()
            flash(f"{formdata['name']} successfully added!")
            return redirect(url_for('admin.db_add'))
        else:
            return 'Error:\n' + str(form.errors)
    return render_template('admin/db_add.html', form=form)

@bp.route('/db/update', methods=['GET', 'POST'])
def db_update():
    from bpaint.models import Color
    form = UpdateForm()
    records = load_db()
    form.recipe.choices = []
    for record in records:
        form.recipe.choices.append((record.id, record.name))
    if not form.recipe.choices:
        return render_template('admin/db_no_update.html')
    if request.method == 'POST':
        # if form.validate_on_submit():
            from bpaint import app, db, uploads
            formdata = form.data
            record = Color.query.filter_by(id=formdata.pop('update')).first()
            os.remove(record.swatch)
            image = formdata.pop('swatch')
            image.filename = secure_filename(image.filename)
            image.resize((200, 200))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], image.filename), 'w'):
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            formdata.pop('csrf_token')
            formdata.pop('submit')
            formdata['swatch'] = os.path.join(url_for('base.static', filename=f'images/{image.filename}'))
            formdata['recipe'] = '|'.join(formdata.get('recipe', []))
            for k, v in formdata.items():
                setattr(record, k, v)
            db.session.add(record)
            db.session.commit()
            if not record.recipe:
                record.recipe = str(record.id)
                db.session.add(record)
                db.session.commit()
            flash(f"{formdata['name']} successfully updated!")
            return redirect(url_for('admin.db_update'))
        # else:
        #     return 'Error:\n' + str(form.errors)
    form.update.choices = form.recipe.choices
    rec_id = request.args.get('rec_id')
    if rec_id:
        record = Color.query.filter_by(id=rec_id).first().__dict__
    else:
        record = None
    return render_template('admin/db_update.html', form=form, rec_id=rec_id, record=record)

@bp.route('/db/delete', methods=['GET', 'POST'])
def db_delete():
    form = DeleteForm()
    records = load_db()
    form.delete.choices = []
    for record in records:
        form.delete.choices.append((record.id, record.name))
    if not form.delete.choices:
        return render_template('admin/db_no_delete.html')
    if request.method == 'POST':
        # if form.validate_on_submit():
            if request.form.get('delete'):
                from bpaint import db
                from bpaint.models import Color
                formdata = form.data
                record = Color.query.filter_by(id=formdata['delete']).first()
                os.remove(record.swatch)
                db.session.delete(record)
                db.session.commit()
                flash('Delete Successful!')
                return redirect(url_for('admin.db_delete'))
            else:
                flash('Please choose a record to delete.')
                return redirect(url_for('admin.db_delete'))
        # else:
        #     return 'Error:\n' + str(form.errors)
    return render_template('admin/db_delete.html', form=form)

@bp.route('/db/<string:next_action>/db_fetch')
def db_fetch(next_action):
    from bpaint.models import Color
    form = AddToDatabaseForm()
    records_all = Color.query.all()
    return render_template('admin/db_fetch.html', records=records_all, next_action=next_action, form=form)

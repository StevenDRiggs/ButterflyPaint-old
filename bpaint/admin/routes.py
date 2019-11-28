import os

from flask import Blueprint, flash, redirect, render_template, request, url_for

from PIL import Image, ImageFile

from werkzeug.utils import secure_filename

from wtforms import IntegerField, SubmitField

from bpaint.admin.forms import AddToDatabaseForm, DeleteForm, UpdateForm

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')


def load_db(rec_id=None):
    from bpaint.models import Color
    if not rec_id:
        records_all = Color.query.all()
    else:
        records_all = Color.query.filter_by(rec_id).all()
    return records_all

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
    ingredients = []
    images = dict()
    for record in records:
        ingredients.append((record.name, record.swatch))
    if len(ingredients) < 2:
        ingredients = []
    else:
        for record in records:
            setattr(AddToDatabaseForm, record.name, IntegerField(record.name, default=0))
            images[record.name] = record.swatch
        setattr(AddToDatabaseForm, 'submit2', SubmitField('Add Color'))
        form = AddToDatabaseForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            from bpaint import app, db, uploads
            from bpaint.models import Color
            formdata = form.data
            print(f'\n{formdata=}\n')
            image_file = formdata.pop('swatch')
            image_file.filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            with open(image_path, 'w'):
                image_file.save(image_path)
            ImageFile.LOAD_TRUNCATED_IMAGE = True
            with Image.open(image_path) as image:
                image = image.resize((200, 200))
                image.save(image_path)
            formdata.pop('csrf_token')
            formdata.pop('submit')
            formdata.pop('submit2', None)
            db_entry = dict()
            db_entry['medium'] = formdata.pop('medium')
            db_entry['name'] = formdata.pop('name')
            db_entry['pure'] = formdata.pop('pure')
            db_entry['swatch'] = url_for('static', filename=f'images/{image_file.filename}')
            recipe = [(color, quantity) for color in records for quantity in formdata.values() if formdata.get(color.name) == quantity and quantity > 0]
            db_entry['recipe'] = recipe
            if not db_entry['recipe']:
                del db_entry['recipe']
            color = Color(**db_entry)
            db.session.add_all([color, *color.recipe])
            db.session.commit()
            return redirect(url_for('admin.db_add'))
        else:
            return 'Error:\n' + str(form.errors)
    return render_template('admin/db_add.html', form=form, images=images)

@bp.route('/db/update')
def db_update():
    records = load_db()
    choices = [{'id': record.id, 'name': record.name, 'swatch': record.swatch} for record in records]
    return render_template('admin/db_update_choices.html', choices=choices)

@bp.route('/db/update/<int:rec_id>', methods=['GET', 'POST'])
def db_update_color(rec_id):
    form = UpdateForm()
    records = load_db()


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

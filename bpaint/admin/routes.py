import os

from flask import Blueprint, flash, redirect, render_template, request, url_for

from PIL import Image, ImageFile

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from wtforms import IntegerField, SubmitField

from bpaint.admin.forms import AddToDatabaseForm, DeleteForm, UpdateDatabaseForm

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')



def load_db(rec_id=None):
    from bpaint.models import Color
    records_all = Color.query.filter_by(id=rec_id).all() if rec_id else Color.query.all()
    return records_all

@bp.route('/')
def admin():
    return render_template('admin/index.html')

@bp.route('/db/')
def db_home():
    return render_template('admin/db_home.html')

@bp.route('/db/<string:operation>', methods=['GET', 'POST'])
@bp.route('/db/<string:operation>/<int:rec_id>', methods=['GET', 'POST'])
def db_add_update(*, operation=None, rec_id=None):
    records = load_db()
    form = None

    if operation == 'add':
        form_type = AddToDatabaseForm
        dest_get = 'admin/db_add.html'
        label = 'Add'
    elif operation == 'update':
        if not rec_id:
            choices = [{'id': record.id, 'name': record.name, 'swatch': record.swatch} for record in records]
            return render_template('admin/db_update_choices.html', choices=choices)
        else:
            form_type = UpdateDatabaseForm
            dest_get = 'admin/db_update.html'
            label = 'Update'
            del records[(rec_check := list(map(lambda r: r.id == rec_id, records))).index(True)]
    elif operation == 'delete':
            choices = [{'id': record.id, 'name': record.name, 'swatch': record.swatch} for record in records]
            return render_template('admin/db_delete_choices.html', choices=choices)
    else:
        flash('Error: Invalid Database Operation')
        return redirect(url_for('.db_home'))

    ingredients = []
    images = dict()
    current = None
    for record in records:
        ingredients.append((record.name, record.swatch))

    if form_type is AddToDatabaseForm and len(ingredients) < 2:
        ingredients = []
    else:
        if form_type is AddToDatabaseForm:  # len(ingredients) >= 2
            rec = None
            default = lambda _: 0
        else:  # form_type is UpdateDatabaseForm
            rec = load_db(rec_id)[0]
            rec_recipe = dict(zip(rec.ingredients, rec.quantities))
            default = lambda r: rec_recipe.get(r.id, 0)

        for record in records:
            setattr(form_type, record.name, IntegerField(record.name, default=default(record)))
            images[record.name] = record.swatch
        setattr(form_type, 'submit2', SubmitField(f'{label} Color'))

        if rec:  # True only if form_type is UpdateDatabaseForm
            prefill = rec.formdict()
            form = form_type(obj=prefill)
            current = (rec.swatch, rec.name)
            if hasattr(form, rec.name):
                exec(f'del form.{rec.name}')

    if not form:
        form = form_type()

    if request.method == 'POST':
        if form.validate_on_submit():
            from bpaint import app, db, uploads
            from bpaint.models import Color

            formdata = form.data
            db_entry = dict()
            color = Color.query.filter_by(id=rec_id).one() if rec_id else None

            formdata.pop('csrf_token')
            formdata.pop('submit')
            formdata.pop('submit2', None)

            db_entry['medium'] = formdata.pop('medium')
            db_entry['name'] = formdata.pop('name')
            db_entry['pure'] = formdata.pop('pure')
            if db_entry['pure']:
                db_entry['recipe'] = None
            else:
                db_entry['recipe'] = [(color, quantity) for color in records for quantity in formdata.values() if formdata.get(color.name) == quantity and quantity > 0]
            if not db_entry['recipe']:
                del db_entry['recipe']

            if formdata['swatch']:
                image_file = formdata.pop('swatch')
                image_file.filename = secure_filename(image_file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
                with open(image_path, 'w'):
                    image_file.save(image_path)
                ImageFile.LOAD_TRUNCATED_IMAGE = True
                with Image.open(image_path) as image:
                    image = image.resize((200, 200))
                    image.save(image_path)
                db_entry['swatch'] = url_for('static', filename=f'images/{image_file.filename}')
            else:
                db_entry['swatch'] = color.swatch

            if rec_id:
                for k,v in db_entry.items():
                    setattr(color, k, v)

            if not color:
                color = Color(**db_entry)
            
            db.session.add_all([color, *color.recipe])
            db.session.commit()

            flash(f"{label} '{color.name}' Successful.")

            if rec_id:
                return redirect(url_for('admin.db_home') + 'update')
            return redirect(request.path)

        else:  # not form.validate_on_submit()
            flash(str(form.errors))
            return redirect(request.path)

    return render_template(dest_get, form=form, images=images, current=current)

@bp.route('/db/delete/<int:rec_id>', methods=['GET', 'POST'])
def db_delete_verify(rec_id, confirmed=False):
    form = DeleteForm()
    if form.data['cancel']:
        return redirect(url_for('.db_home'))
    rec = load_db(rec_id)[0]
    current = (rec.swatch, rec.name)
    confirmed = form.data['submit']

    if request.method == 'POST' and confirmed:
        rec.delete()

        flash(f'{rec.name} Successfully Deleted.')
        return redirect(url_for('.db_home'))

    return render_template('admin/db_delete_confirm.html', form=form, images={}, current=current)

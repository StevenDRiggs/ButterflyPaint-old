from flask import Blueprint, flash, render_template, request

from wtforms.fields import IntegerField

bp = Blueprint('inv', __name__, static_folder='static', template_folder='templates', url_prefix='/inventory')


@bp.route('/', methods=['GET', 'POST'])
def inv():
    from bpaint import db
    from bpaint.inv.forms import InventoryForm

    records = set(db.session.execute('select color.id as id, color.name as name, color.swatch as swatch, inventory.quantity as quantity from color join inventory on id = inventory.color_id').fetchall())

    for record in records:
        if not hasattr(InventoryForm, record.name):
            setattr(InventoryForm, record.name, IntegerField(record.name, default=record.quantity))
        else:
            getattr(InventoryForm, record.name).default = record.quantity

    form = InventoryForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            formdata = form.data
            formdata.pop('csrf_token')
            formdata.pop('update')

            for field_id in formdata:
                record = Inventory.query.filter(Inventory.color_id == int(field_id)).one()
                record.quantity = formdata[field_id]
                db.session.add(record)

            db.session.commit()
            flash('Inventory updated.')

        else:  # not form.validate_on_submit()
            flash(str(form.errors))
            return redirect(request.path)

    return render_template('inv/index.html', form=form, records=records)

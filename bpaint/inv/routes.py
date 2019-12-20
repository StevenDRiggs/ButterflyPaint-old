from flask import Blueprint, render_template

bp = Blueprint('inv', __name__, static_folder='static', template_folder='templates', url_prefix='/inventory')


@bp.route('/', methods=['GET', 'POST'])
def inv():
    from bpaint import db
    from bpaint.inv.forms import InventoryForm

    records = db.session.execute('select color.id as id, color.name as name, color.swatch as swatch, inventory.quantity as quantity from color join inventory on id = inventory.color_id').fetchall()
    # for rec in records:
        


    return render_template('inv/index.html')

from flask import Blueprint # , flash, redirect, render_template, request

# from wtforms.fields import IntegerField, SubmitField

bp = Blueprint('inv', __name__, static_folder='static', template_folder='templates', url_prefix='/inventory')


# @bp.route('/', methods=['GET', 'POST'])
# def inv():
#     from bpaint import Color, db, Inventory
#     from bpaint.inv.forms import InventoryForm

#     if request.method == 'GET':
#         color_ids = map(lambda x: x.values()[0], db.session.execute('select id from color').fetchall())
#         inv_color_ids = set(map(lambda y: y.values()[0], db.session.execute('select color_id from inventory').fetchall()))

#         for color_id in color_ids:
#             if color_id not in inv_color_ids:
#                 db.session.add(Inventory(color_id, 0))
#         db.session.commit()

#         display = db.session.execute('select color.name as name, color.swatch as swatch, inventory.quantity as quantity from color join inventory on color.id = inventory.color_id').fetchall()
#         images = dict()

#         if hasattr(InventoryForm, 'update'):
#             delattr(InventoryForm, 'update')
#         for item in display:
#             if not hasattr(InventoryForm, item.name):
#                 setattr(InventoryForm, item.name, IntegerField(item.name, default=item.quantity))
#             images[item.name] = item.swatch
#         setattr(InventoryForm, 'update', SubmitField('Update Inventory'))

#         form = InventoryForm()

#         return render_template('inv/index.html', form=form, images=images)

#     elif request.method == 'POST':
#         form = InventoryForm()
#         formdata = form.data

#         formdata.pop('csrf_token')
#         formdata.pop('update')

#         for name, quantity in formdata.items():
#             with db.session.no_autoflush:
#                 color_id = Color.query.filter(Color.name == name).one().id
#                 curr_inv = Inventory.query.filter(Inventory.color_id == color_id).first()
#                 if not curr_inv:
#                     curr_inv = Inventory(color_id, quantity)
#                 else:
#                     curr_inv.quantity = quantity
#                 db.session.add(curr_inv)
#             delattr(InventoryForm, name)
#         db.session.commit()
#         if hasattr(InventoryForm, 'update'):
#             delattr(InventoryForm, 'update')

#         flash('Inventory successfully updated')
#         return redirect(request.path)

#     else:  # request.method is neither 'GET' nor 'POST'
#         flash('Illegal inventory operation')
#         return redirect(request.path)
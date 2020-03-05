# from flask import Blueprint # , render_template

# from bpaint.config import MEDIUM_CHOICES


bp = Blueprint('details', __name__, static_folder='static', template_folder='templates', url_prefix='/details')


# @bp.route('/<int:rec_id>')
# def details(rec_id):
#     from bpaint import load_db

#     rec = load_db(rec_id)[0]

#     colors = {
#             'current': {
#                 'medium': dict(MEDIUM_CHOICES)[rec.medium],
#                 'name': rec.name,
#                 'pure': rec.pure,
#                 'swatch': rec.swatch,
#                 'recipe': {
#                     recipe.ingredient_id: {
#                         'ingredient_name': recipe.ingredient_name,
#                         'quantity': recipe.quantity,
#                         'swatch': load_db(recipe.ingredient_id)[0].swatch,
#                         }
#                     for recipe in rec.recipe
#                     },
#                 'used_in': {
#                     color.id: {
#                         'name': color.name,
#                         'swatch': color.swatch,
#                         }
#                     for color in rec.used_in
#                     }
#                 }
#             }


#     return render_template('details/index.html', colors=colors)

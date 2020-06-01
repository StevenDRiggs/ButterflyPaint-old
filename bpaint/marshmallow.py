
'''
Marshmallow
--------------
'''

from bpaint.model import *

from flask_marshmallow import Marshmallow

from bpaint import app

ma = Marshmallow(app)

# Sample Marshmallow Schemas, us this method to make yours

class UserSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
        model = User
        load_instance = True


class ColorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Color
        load_instance = True
        include_relationships = True


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
        include_fk = True


class InventoryAutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        load_instance = True
        include_fk = True

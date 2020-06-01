
'''
Marshmallow
--------------
'''

from bpaint.model import *

from flask_marshmallow import Marshmallow

from bpaint import app

ma = Marshmallow(app)

# Sample Marshmallow Schemas, us this method to make yours

class UserSchema(ma.SQLAlchemySchema):
   class Meta:
        model = User
        load_instance = True


class ColorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Color
        load_instance = True


class RecipeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recipe
        load_instance = True


class InventorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Inventory
        load_instance = True

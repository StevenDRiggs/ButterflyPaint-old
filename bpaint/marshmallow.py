
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


class ColorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Color


class RecipeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recipe


class InventorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Inventory

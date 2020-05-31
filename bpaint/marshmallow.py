
'''
Marshmallow
--------------
'''

from bpaint.model import *

from flask_marshmallow import Marshmallow

from bpaint import app

ma = Marshmallow(app)

# Sample Marshmallow Schemas, us this method to make yours

class UserSchema(ma.Schema):
   class Meta:
       model = User

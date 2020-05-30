
'''
Marshmallow
--------------
'''

from bpaint.model import *

from flask_marshmallow import Marshmallow

from bpaint import app

ma = Marshmallow(app)

# Sample Marshmallow Schemas, us this method to make yours

class BookSchema(ma.Schema):
   class Meta:
       model = Book
   include_fk = True #This includes foreignkeys

class AuthorSchema(ma.Schema):
   class Meta:
       model = Author
   include_fk = True #This includes foreignkeys
   books = ma.Nested("BookSchema", many=True)
        

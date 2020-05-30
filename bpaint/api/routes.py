
'''
api
--------------
'''
from flask import Blueprint, request, render_template, redirect, url_for

from bpaint.marshmallow import AuthorSchema

from bpaint.model import *

api = Blueprint('api', __name__, url_prefix='/api')

author_schema = AuthorSchema(exclude=['id'])

@api.route('/users')
def author():
    author = Author.query.first()
    return author_schema.jsonify(author)
        
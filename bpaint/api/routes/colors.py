
'''
colors
--------------
'''
from flask import Blueprint, request, render_template, redirect, url_for

from flask_login import login_required

from bpaint.marshmallow import ColorSchema, RecipeSchema

from bpaint.model import *

colors_api = Blueprint('colors', __name__, url_prefix='/colors')

color_schema = ColorSchema(many=True)

@colors_api.route('/')
# @login_required
def colors():
    colors = Color.query.all()
    print(colors)
    cs = color_schema.dumps(colors)
    print(cs)
    return cs
        

@colors_api.route('/<int:id>')
# @login_required
def show_color(id):
    color = Color.query.filter(Color.id == id)
    cs = color_schema.dumps(color)
    print(cs)
    return cs

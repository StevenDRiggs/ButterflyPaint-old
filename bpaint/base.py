from flask import Blueprint

bp = Blueprint('base', __name__, template_folder='templates', static_folder='static')

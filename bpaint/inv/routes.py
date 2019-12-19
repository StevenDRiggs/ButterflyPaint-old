from flask import Blueprint, render_template

bp = Blueprint('inv', __name__, static_folder='static', template_folder='templates', url_prefix='/inventory')


@bp.route('/')
def inv():
    from bpaint.models import Color, Inventory
    
    return render_template('inv/index.html')

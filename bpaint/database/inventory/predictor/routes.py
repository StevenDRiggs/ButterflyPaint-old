from flask import Blueprint, render_template


bp = Blueprint('predictor', __name__, url_prefix='/predictor', template_folder='templates')


@bp.route('/')
def recipe_predictor():
    return render_template('predictor/predictor.html')

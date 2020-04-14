from flask import Blueprint


bp = Blueprint('predictor', __name__, url_prefix='/predictor')


@bp.route('/')
def recipe_predictor():
    return __name__

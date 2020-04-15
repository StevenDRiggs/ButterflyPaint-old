from flask import Blueprint, render_template


bp = Blueprint('splash', __name__, template_folder='templates')


@bp.route('/')
def splash():
    return render_template('splash/splash.html')

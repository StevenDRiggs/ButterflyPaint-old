# from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint('splash', __name__, template_folder='templates', static_folder='static', static_url_path='/splash/static')

splash_seen = False


@bp.route('/')
def splash():
    global splash_seen
    if not splash_seen:
        splash_seen = True
        return render_template('splash/splash.html')
    else:
        return redirect(url_for('splash.index'))

@bp.route('/index')
def index():
    return render_template('splash/index.html')

@bp.route('/replay')
def replay():
    global splash_seen
    splash_seen = False
    return redirect(url_for('splash.splash'))

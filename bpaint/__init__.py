
'''
bpaint
--------------
'''
#Basic Flask Requirements
from flask import Flask, request, render_template, url_for, redirect, session, flash, Response, make_response, send_file, send_from_directory, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

import os

from bpaint.model import db

#instance of app
app = Flask(__name__)

#cookie generator
app.secret_key = os.urandom(24)

#configs
app.config.from_pyfile('config.cfg')

db.init_app(app)

from bpaint import filters
from bpaint.model import User
from bpaint.methods import do_login

#Flask Login Setup
LOGINMANAGER = LoginManager()
LOGINMANAGER.init_app(app)
LOGINMANAGER.login_view = 'index'

#Loading Users to Flask-Login
@LOGINMANAGER.user_loader
def load_user(user_id):
    '''
    Queries and loads all users from the db module.
    '''
    #Getting all users from the database
    return User.query.get(user_id)

#TODO: Register more blueprints like this
# Check the blueprint folder for more info
from bpaint.api.routes import api
app.register_blueprint(api)

#Sample App Context Function
@app.context_processor
def app_wide_variables():
    '''
    Function takes no argument,
    returns variables that are accessible everywhere in the app

    #TODO: pass *kwargs to dict
    '''
    return dict()

#Sample Index Route or Login Route
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Index function takes no argument,
    routes to the '/' page and holds the login logic.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('protected_route'))
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        if do_login(user, password):
            if 'next' in request.args:
                return redirect(request.args['next'])
            return redirect(url_for('protected'))
        flash('Invalid Login Details!')
    return render_template("login.html")

#Sample protected route
@app.route('/protected-route')
@login_required
def protected_route():
    '''
    Sample protected route, change it to your test
    '''
    return render_template('protected.html')


#Sample Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('protected_route'))

#Sample 404 error page
@app.errorhandler(404)
def page404(e):
    return render_template('404.html')
        
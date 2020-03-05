# from flask import Blueprint # , redirect, render_template, url_for

bp = Blueprint('search', __name__, url_prefix='/search', template_folder='templates')


# @bp.route('/')
# def search():
#     return redirect(url_for('text_search.text_search'))

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from bpaint.admin.routes import bp as admin_bp
from bpaint.inv.routes import bp as inv_bp
from bpaint.search.pic.routes import bp as pic_search_bp
from bpaint.search.text.routes import bp as text_search_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

app.register_blueprint(admin_bp)
app.register_blueprint(inv_bp)
app.register_blueprint(pic_search_bp)
app.register_blueprint(text_search_bp)

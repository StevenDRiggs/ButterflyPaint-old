from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from bpaint.admin.routes import bp as admin_bp
from bpaint.inv.routes import bp as inv_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

app.register_blueprint(admin_bp)
app.register_blueprint(inv_bp)

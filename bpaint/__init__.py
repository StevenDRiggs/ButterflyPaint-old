from flask import Flask

#from flask_sqlalchemy import SQLAlchemy

#from flask_uploads import UploadSet, configure_uploads, patch_request_class

from sqlalchemy import event
from sqlalchemy.engine import Engine

from .config import Config

@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()

app = Flask(__name__)
app.config.from_object(Config)

uploads = UploadSet(name='images', extensions=app.config['ALLOWED_FILES'], default_dest=lambda _: '/static/images')
configure_uploads(app, uploads)
patch_request_class(app, 10 * 1024 * 1024)

db = SQLAlchemy(app=app, session_options={'expire_on_commit':False})
#from bpaint.models import Color, Inventory, Recipe
db.create_all()
db.session.commit()

#from .base import bp as base_bp
#from .admin.routes import bp as admin_bp, load_db
#from .details.routes import bp as details_bp
#from .inv.routes import bp as inv_bp
#from .search.routes import bp as search_bp
#from .search.pic.routes import bp as pic_search_bp
#from .search.text.routes import bp as text_search_bp
#from .splash.routes import bp as splash_bp

app.register_blueprint(base_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(details_bp)
app.register_blueprint(inv_bp)
app.register_blueprint(search_bp)
app.register_blueprint(pic_search_bp)
app.register_blueprint(text_search_bp)
app.register_blueprint(splash_bp)

from flask import Flask

from .routes import bp as base_bp
from .index import index_bp, splash_bp
from .database import database_bp, inventory_bp, search_bp, predictor_bp


app = Flask(__name__)

app.register_blueprint(base_bp)
app.register_blueprint(index_bp)
app.register_blueprint(splash_bp)
app.register_blueprint(database_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(search_bp)
app.register_blueprint(predictor_bp)
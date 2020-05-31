
'''
MODEL
--------------
'''
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password = gph(password)
        return True
        
    def is_verified(self, password):
        return cph(self.password, password)
        

class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String)
    image_url = db.Column(db.String, nullable=False)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_color_id = db.Column(db.Integer)
    ingredient_color_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, nullable=False)


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    in_stock = db.Column(db.Integer, default=0)
    minimum_stock = db.Column(db.Integer, default=-1)
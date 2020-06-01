
'''
MODEL
--------------
'''
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password = gph(password)
        return True
        
    def is_verified(self, password):
        return cph(self.password, password)
        

class Color(db.Model):
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String)
    image_url = db.Column(db.String, nullable=False)

    inventory = db.relationship('Inventory', uselist=False, lazy=True)

    recipe = db.relationship('Color',
            secondary='recipes',
            primaryjoin='colors.c.id==recipes.c.parent_color_id',
            secondaryjoin='colors.c.id==recipes.c.ingredient_color_id'
    )


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    parent_color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    ingredient_color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    quantity = db.Column(db.Integer, nullable=False)


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    in_stock = db.Column(db.Integer, default=0)
    minimum_stock = db.Column(db.Integer, default=-1)


'''
MODEL
--------------
'''
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as gph, check_password_hash as cph

from cryptography.fernet import Fernet


try:
    with open('key', 'rb') as f:
        key = f.read()
except FileNotFoundError:
    with open('key', 'wb') as f:
        key = Fernet.generate_key()
        f.write(key)
finally:
    fernet = Fernet(key)

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    __username = db.Column(db.Binary, nullable=False, unique=True)
    __email = db.Column(db.Binary)
    __password = db.Column(db.Binary, nullable=False)

    @property
    def username(self):
        return fernet.decrypt(self.__username).decode('utf-8')

    @username.setter
    def username(self, username):
        self.__username = fernet.encrypt(username.encode('utf-8'))

    @property
    def email(self):
        return fernet.decrypt(self.__email).decode('utf-8')

    @email.setter
    def email(self, email):
        self.__email = fernet.encrypt(email.encode('utf-8'))

    @property
    def password(self):
        return '<encrypted>'

    @password.setter
    def password(self, password):
        self.__password = fernet.encrypt(gph(password).encode('utf-8'))
        
    def is_verified(self, password):
        return cph(fernet.decrypt(self.__password).decode('utf-8'), password)

    def __repr__(self):
        return f'<User: {self.id=}, {self.username=}, {self.email=}, {self.password=}>'
        

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
            secondaryjoin='colors.c.id==recipes.c.ingredient_color_id',
            join_depth=1
    )

    def __repr__(self):
        return f'<Color: {self.name=}, {self.recipe=}>'


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    parent_color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    ingredient_color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Recipe: {Color.query(Color.id == self.ingredient_color_id).first().name} (x{self.quantity})'


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'))
    in_stock = db.Column(db.Integer, default=0)
    minimum_stock = db.Column(db.Integer, default=-1)

from sqlalchemy.ext.associationproxy import association_proxy

from bpaint import db


class Recipe(db.Model):
    base_id = db.Column(db.Integer, db.ForeignKey('color.id'), primary_key=True)
    ingredients = db.relationship('Color')
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'Recipe({self.base_id=}, {self.ingredients=}, {self.quantity=})'

class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    pure = db.Column(db.Boolean, default=False, nullable=False)
    recipe = db.relationship(Recipe,
            primaryjoin=id==Recipe.base_id)
    swatch = db.Column(db.String(25), nullable=False, unique=True)

    def __repr__(self):
        return f'Color({self.name=} {self.recipe=})'



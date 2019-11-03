from sqlalchemy.ext.associationproxy import association_proxy

from bpaint import db


class Recipe(db.Model):
    base_id = db.Column(db.Integer, db.ForeignKey('color.id'), primary_key=True)
    ingredients = db.relationship('Color')
    quantity = db.Column(db.Integer)

    def __init__(self, ingredient, quantity):
        print(f'{self.base_id=}\n{self.ingredients=}\n{self.quantity=}\n{ingredient=}\n{quantity=}')
        self.ingredients = ingredient
        self.quantity = quantity

    def __repr__(self):
        return f'{self.ingredients} x{self.quantity}'

class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    pure = db.Column(db.Boolean, default=False, nullable=False)
    _recipe = db.relationship(Recipe,
            primaryjoin=id==Recipe.base_id,
            join_depth=1)
    recipe = association_proxy('_recipe', 'ingredients',
        creator = lambda _: _)
    swatch = db.Column(db.String(25), nullable=False, unique=True)

    def __init__(self, medium, name, pure, recipe=None, *, swatch):
        self.medium = medium
        self.name = name
        self.pure = pure
        self.swatch = swatch

        if self.pure:
            self.recipe = [Recipe(self, 1)]
        else:
            for ingredient, quantity in recipe:
                self.recipe.append(Recipe(ingredient, quantity))

    def __repr__(self):
        return f'Color({self.name})'



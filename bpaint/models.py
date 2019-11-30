from sqlalchemy.ext.associationproxy import association_proxy

from bpaint import db


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    pure = db.Column(db.Boolean, nullable=False, default=True)
    swatch = db.Column(db.String(25), nullable=False, unique=True)

    recipe = db.relationship('Recipe',
        primaryjoin='Color.id==Recipe.base_id',
        uselist=True,
        join_depth=1,
        lazy='joined'
        )

    ingredients = association_proxy('recipe', 'ingredient_id')
    quantities = association_proxy('recipe', 'quantity')

    def __init__(self, medium, name, *, pure=True, recipe=[], swatch):
        self.medium = medium.upper()
        self.name = name
        self.pure = False if len(recipe) > 1 else True
        self.swatch = swatch

        db.session.add(self)
        db.session.flush([self])

        if self.pure:
            recipe = [(self, 1)]
        for entry in recipe:
            self.recipe.append(Recipe(self, entry))

    def __repr__(self):
        return f'<Color({self.name})>'


class Recipe(db.Model):
    base_id = db.Column(db.Integer, db.ForeignKey('color.id'), primary_key=True, autoincrement=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('color.id'), primary_key=True, autoincrement=False)
    ingredient_name = db.Column(db.String, db.ForeignKey('color.name'))
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, base, ingredient_tuple):
        super().__init__()
        self.base_id = base.id
        self.ingredient_id = ingredient_tuple[0].id
        self.ingredient_name = ingredient_tuple[0].name
        self.quantity = ingredient_tuple[1]

    def __repr__(self):
        return f'{self.ingredient_name}(x{self.quantity})'


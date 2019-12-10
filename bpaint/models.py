import os

from PIL import Image, ImageFile

from sqlalchemy.ext.associationproxy import association_proxy

from bpaint import app, db


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    _pure = db.Column(db.Boolean, nullable=False, default=True)
    swatch = db.Column(db.String(25), nullable=False, unique=True)

    _recipe = db.relationship('Recipe',
        primaryjoin='Color.id==Recipe.base_id',
        uselist=True,
        join_depth=1,
        lazy='joined',
        cascade='all, delete-orphan'
        )

    ingredients = association_proxy('_recipe', 'ingredient_id')
    quantities = association_proxy('_recipe', 'quantity')

    @property
    def recipe(self):
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        if self._pure:
            recipe = [(self, 1)]
        self._recipe = []
        for entry in recipe:
            self._recipe.append(Recipe(self, entry))

    @property
    def pure(self):
        return self._pure

    @pure.setter
    def pure(self, pure):
        self._pure = pure
        if self._pure:
            self.recipe = [(self, 1)]

    def __init__(self, medium, name, *, pure=True, recipe=[], swatch):
        self.medium = medium.upper()
        self.name = name
        self._pure = False if len(recipe) > 1 else True
        self.swatch = swatch

        db.session.add(self)
        db.session.flush([self])

        if self._pure:
            recipe = [(self, 1)]
        for entry in recipe:
            self._recipe.append(Recipe(self, entry))

    def formdict(self):
        class FormDict(object):
            medium = str
            name = str
            pure = bool

        filename = self.swatch.rsplit('/', 1)[1]

        fd = FormDict()

        fd.medium = self.medium
        fd.name = self.name
        fd.pure = self._pure

        return fd

    def delete(self):
        def spiderweb_delete(ingredient_id):
            color = Color.query.filter_by(id=ingredient_id).one()
            if color.pure:
                return color
            else:
                ingredients = color.ingredients
                to_delete = set()
                for ingredient_id in ingredients:
                    to_delete.add(spiderweb_delete(ingredient_id))
                return to_delete

        ingredients = self.ingredients
        to_delete = set()
        for ingredient_id in ingredients:
            to_delete.add(spiderweb_delete(ingredient_id))
        db.session.delete_all(list(to_delete))
        db.session.commit()


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


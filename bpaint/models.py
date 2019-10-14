from bpaint import db


link = db.Table(
    db.Column('color_id', db.Integer, db.ForeignKey('color.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('color.id'), primary_key=True),
    db.Column('quantity', db.Integer)
)


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(50), nullable=False) #, unique=True)
    pure = db.Column(db.Boolean, default=False, nullable=False)
    recipe = db.relationship('Color', secondary=link)
    swatch = db.Column(db.String(25), nullable=False) #, unique=True)

    def __repr__(self):
        mix = self.name if self.pure else self.recipe
        return f'{self.name}: {mix}'



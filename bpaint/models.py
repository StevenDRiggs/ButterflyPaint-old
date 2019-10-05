from bpaint import db


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    pure = db.Column(db.Boolean, default=False, nullable=False)
    recipe = db.Column(db.Text, nullable=False)
    swatch = db.Column(db.String(25), nullable=False, unique=True)

    def __repr__(self):
        mix = self.name if self.pure else self.recipe
        return f'{self.name}: {mix}'

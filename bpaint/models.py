from bpaint import db


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String(2), nullable=False)
    color_num = db.Column(db.Integer)
    name = db.Column(db.String(50), unique=True)
    pure = db.Column(db.Boolean, default=False, nullable=False)
    recipe = db.Column(db.Text, nullable=False, unique=True)
    image = db.Column(db.String(25), nullable=False, unique=True)

    def __repr__(self):
        if self.name:
            return f'{self.color_num}. {self.name}'
        else:
            return f'{self.color_num}. {self.recipe}'

from flask import url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms.fields import BooleanField, IntegerField, RadioField, SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
import wtforms.widgets as widgets

from bpaint import uploads
from bpaint.config import medium_choices


class AddToDatabaseForm(FlaskForm):
    medium = RadioField('Medium', choices=medium_choices)
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    pure = BooleanField('Pure')
    swatch = FileField('Swatch', validators=[FileAllowed(uploads)])
    submit = SubmitField('Add Color')

    def __init__(self, rec_id=None):
        super().__init__()


class UpdateDatabaseForm(AddToDatabaseForm):
    submit = SubmitField('Update Color')

    def __init__(self, rec_id):
        from bpaint.admin.routes import load_db
        record = load_db(rec_id)
        self.medium.default = record.medium
        self.name.default = record.name
        self.pure.default = record.pure
        self.swatch.default = record.swatch
        super().__init__()


class DeleteForm(FlaskForm):
    delete = RadioField('delete')
    submit = SubmitField('Delete Color')

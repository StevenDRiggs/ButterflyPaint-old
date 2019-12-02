from flask import url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms.fields import BooleanField, IntegerField, RadioField, SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from bpaint import uploads
from bpaint.config import medium_choices


class AddToDatabaseForm(FlaskForm):
    medium = RadioField('Medium', choices=medium_choices)
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    pure = BooleanField('Pure')
    swatch = FileField('Swatch', validators=[FileAllowed(uploads)])
    submit = SubmitField('Add Color')


class UpdateDatabaseForm(AddToDatabaseForm):
    submit = SubmitField('Update Color')


class DeleteForm(FlaskForm):
    delete = RadioField('delete')
    submit = SubmitField('Delete Color')

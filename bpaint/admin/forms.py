# from flask import url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

# from inspect import getmembers

from wtforms.fields import RadioField, StringField, BooleanField, SubmitField # , IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length # , Optional
from wtforms.widgets import HiddenInput

# from bpaint import uploads
from bpaint.config import MEDIUM_CHOICES


class AddToDatabaseForm(FlaskForm):
    medium = RadioField('Medium', choices=MEDIUM_CHOICES)
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    visible_pure = BooleanField(label='Pure', id='visible-pure')
    pure = BooleanField(label='Pure', id='pure', widget=HiddenInput(), default=False)
    swatch = FileField('Swatch', validators=[FileAllowed(uploads)])
    submit = SubmitField('Add Color')


# class UpdateDatabaseForm(AddToDatabaseForm):
#     submit = SubmitField('Update Color')


# class DeleteForm(FlaskForm):
#     cancel = SubmitField('Cancel')
#     submit = SubmitField('Delete Color')


# ADD_ORIG_MEMBERS = getmembers(AddToDatabaseForm)
# UPDATE_ORIG_MEMBERS = getmembers(UpdateDatabaseForm)

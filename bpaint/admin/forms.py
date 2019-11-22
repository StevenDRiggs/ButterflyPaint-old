from flask import url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

import wtforms.widgets as widgets
from wtforms.fields import BooleanField, IntegerField, RadioField, SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from bpaint import uploads


class AddToDatabaseForm(FlaskForm):
    medium = RadioField('medium', choices=[('OA', 'Oil/Acrylic')])
    name = StringField('name', validators=[DataRequired(), Length(max=50)])
    pure = BooleanField('pure')
    recipe = SelectMultipleField('recipe', widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.CheckboxInput())
    swatch = FileField('swatch', validators=[FileAllowed(uploads)])
    submit = SubmitField('submit')


class UpdateForm(AddToDatabaseForm):
    update = RadioField('')
    submit = SubmitField('submit')


class DeleteForm(FlaskForm):
    delete = RadioField('delete')
    submit = SubmitField('submit')

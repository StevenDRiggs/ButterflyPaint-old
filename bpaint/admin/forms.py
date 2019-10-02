from flask import url_for

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms.fields import BooleanField, IntegerField, RadioField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

from bpaint import uploads


class AddToDatabaseForm(FlaskForm):
    medium = StringField('medium', validators=[DataRequired(), Length(min=2, max=2)])
    name = StringField('name', validators=[DataRequired(), Length(max=40)])
    pure = BooleanField('pure')
    recipe = TextAreaField('recipe', validators=[DataRequired()])
    swatch = FileField('swatch', validators=[FileAllowed(uploads)])

    submit = SubmitField('submit')


class UpdateForm(AddToDatabaseForm):
    update = SelectField('')
    submit = SubmitField('submit')


class DeleteForm(FlaskForm):
    delete = SelectField('delete')

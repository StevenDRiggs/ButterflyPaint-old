from flask import url_for

from flask_uploads import IMAGES, UploadSet

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms.fields import BooleanField, IntegerField, RadioField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class AddToDatabaseForm(FlaskForm):
    medium = StringField('medium', validators=[DataRequired(), Length(min=2, max=2)])
    color_num = IntegerField('color-num', validators=[Optional()])
    name = StringField('name', validators=[DataRequired(), Length(max=40)])
    pure = BooleanField('pure')
    recipe = TextAreaField('recipe', validators=[DataRequired()])
    swatch = FileField('swatch', validators=[DataRequired(), FileAllowed(UploadSet(name='pics', extensions=IMAGES, default_dest='static/images/'))])

    submit = SubmitField('submit')


class UpdateForm(AddToDatabaseForm):
    update = SelectField('', validators=[DataRequired()])
    submit = SubmitField('submit')


class DeleteForm(FlaskForm):
    delete = SelectField('delete', validators=[DataRequired()])
from flask import url_for

from flask_uploads import IMAGES, UploadSet

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms import BooleanField, IntegerField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class AddToDatabaseForm(FlaskForm):
    medium = StringField('medium', validators=[DataRequired(), Length(min=2, max=2)])
    color_num = IntegerField('color-num')
    name = StringField('name', validators=[DataRequired(), Length(max=40)])
    pure = BooleanField('pure')
    recipe = TextAreaField('recipe', validators=[DataRequired()])
    swatch = FileField('swatch', validators=[DataRequired(), FileAllowed(UpdateSet(name='pics', extensions=IMAGES, default_dest=url_for('admin.static')+'/uploads/'))])

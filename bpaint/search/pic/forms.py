from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms.fields import IntegerField, SubmitField
from wtforms.validators import DataRequired

from bpaint import uploads


class PicSearchForm(FlaskForm):
    image_to_search = FileField('Image to Search', validators=[FileAllowed(uploads)])
    threshold = IntegerField('Color Threshold', default=2)
    submit = SubmitField('Search Database')

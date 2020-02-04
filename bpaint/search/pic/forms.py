from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField

from wtforms.fields import BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from bpaint import uploads
from bpaint.config import DEFAULT_PIC_SEARCH_THRESHOLD


class PicSearchForm(FlaskForm):
    image_to_search = FileField('Image to Search', validators=[FileAllowed(uploads)])
    threshold = IntegerField('Color Threshold', default=DEFAULT_PIC_SEARCH_THRESHOLD)
    # heuristic = BooleanField('Heuristic Search', default=True)
    # extra_heuristic = BooleanField('Extra Heuristic Search', default=False)
    submit = SubmitField('Search Database')

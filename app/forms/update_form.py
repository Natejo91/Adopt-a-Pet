from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


class UpdateForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    zipcode = IntegerField('zipcode', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet Name",  validators=[InputRequired(message="Pet Name can't be blank")])
    species = StringField("Species", validators=[InputRequired(message="Species can't be blank")])
    photo_url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")


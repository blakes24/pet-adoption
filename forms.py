from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form to create a new pet."""
    name = StringField("Pet Name",  validators=[InputRequired(message="Pet Name can't be blank")])
    species = StringField("Species", validators=[InputRequired(message="Species can't be blank"), AnyOf(["cat", "dog", "porcupine"], message="the species should be either “cat”, “dog”, or “porcupine”", values_formatter=None)])
    photo_url = StringField("Photo URL", validators=[URL(require_tld=False, message="must be a valid URL"), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="age must be a number from 0 to 30"), Optional()])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit some pet details"""
    photo_url = StringField("Photo URL", validators=[URL(require_tld=False, message="must be a valid URL"), Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = RadioField("Available for adoption", coerce=int, choices=[(1, 'Yes'), (0, 'No')], validators=[InputRequired(message="availability can't be blank")])
    

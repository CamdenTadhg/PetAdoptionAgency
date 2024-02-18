from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField

class AddPetForm(FlaskForm):
    """Form for adding a pet to the database"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")
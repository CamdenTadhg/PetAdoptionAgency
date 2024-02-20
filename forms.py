from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, FileField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, NoneOf, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import IMAGES

def duplicate_image_check(form, field):
    if form.photo_url.data and form.photo_file.data:
        raise ValidationError('You can enter a URL or a file, but not both')

class AddPetForm(FlaskForm):
    """Form for adding a pet to the database"""

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a name")])
    species = StringField("Species", validators=[InputRequired(message="Please enter a species"), NoneOf(values=["cat", "dog"], message="The Modern Menagerie does not include cats or dogs")])
    photo_url = StringField("Photo URL", validators=[URL(message="Please enter a valid URL"), Optional(), duplicate_image_check])
    photo_file=FileField("Photo File", validators=[FileAllowed(['jpg', 'png'], message="Please upload an image file"), duplicate_image_check])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Please enter an age between 0 and 30"), Optional(), ])
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):
    """Form for editing a pet in the database"""

    photo_url = StringField("Photo URL", validators=[URL(message="Please enter a valid URL"), Optional(), duplicate_image_check])
    photo_file=FileField("Photo File", validators=[FileAllowed(['jpg', 'png'], message="Please upload an image file"), duplicate_image_check])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Please enter an age between 0 and 30"), Optional()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available?")


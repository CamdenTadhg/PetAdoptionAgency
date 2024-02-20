from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import exc
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileAllowed

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petagency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug=DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def show_home_page():
    """home page displaying available pets"""
    available_pets = db.session.execute(db.select(Pet).where(Pet.available == True).order_by(Pet.name)).scalars()
    unavailable_pets = db.session.execute(db.select(Pet).where(Pet.available == False).order_by(Pet.name)).scalars()
    return render_template("home.html", available_pets=available_pets, unavailable_pets=unavailable_pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """form for adding pet; adding handler"""

    form = AddPetForm()

    if form.validate_on_submit():
        labels = ['name', 'species', 'photo_url', 'age', 'notes', 'available']
        data = {l:v for (l, v) in zip(labels, form.data.values())}
        pet = Pet(**data)
        try:
            db.session.add(pet)
            db.session.commit()
            flash(f"Added {form.name.data}, the {form.species.data}")
        except exc.IntegrityError:
            db.session.rollback()
            flash(f'{form.name.data}, the {form.species.data} is already in the system')
            return render_template("pet_add_form.html", form=form)
        return redirect("/")
    else:
        return render_template("pet_add_form.html", form=form)

@app.route("/<int:pet_id_number>", methods=["GET"])
def show_pet(pet_id_number):
    """show pet details"""

    pet = Pet.query.get_or_404(pet_id_number)
    return render_template("pet_details.html", pet=pet)

@app.route("/<int:pet_id_number>/edit", methods=["GET", "POST"])
def edit_pet(pet_id_number):
    """form for editing pet; editing handler"""

    pet = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet.name} updated!")
        return redirect(f"/{pet.id}")
    else:
        return render_template("pet_edit_form.html", pet=pet, form=form)



# 1 add testing for all
    # why isn't my test database being used? 
    # why isn't my default value working? 
    # why are my other tests failing? 
# 2 add a new field for a photo upload to save to the /static directory; only one of the photo fields can be filled out (use validation)
    # process uploaded photo to save to a file path
    # insert filepath appropriately into pet instance
    # ensure only one of the two image fields can be completed

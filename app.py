from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

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
    pets = db.session.execute(db.select(Pet).order_by(Pet.name)).scalars()
    return render_template("home.html", pets=pets)

# 14 create homepage
# 13 create add pet form
# 12 create handler for add pet form
# 11 add validation
# 10 add display/edit form
# 9 handle edit form
# 8 refactor your code
# 7 add flash for feedback after adding or editing
# 6 divide the homepage into available and no-longer-available
# 5 add testing for all
# 4 add Bootstrap and a simple theme
# 3 reduce duplication by using Jinja2's "include" directive and factor out common code
# 2 instantiate the pet more diretly using the dictionary of values
# 1 add a new field for a photo upload to save to the /static directory; only one of the photo field can be filled out (use validation)
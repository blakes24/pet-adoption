from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "whatever23424"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_form():
    """Renders add form (GET) or handles add form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        
        flash(f"New pet added: {name} ({species})")
        return redirect('/')
    else:
        return render_template("add-pet.html", form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_info(pet_id):
    """Renders pet details and edit form (GET) or handles add form submission (POST)"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        
        flash(f"{pet.name}'s information has been updated")
        return redirect('/')
    else:
        return render_template("pet-details.html", form=form, pet=pet)

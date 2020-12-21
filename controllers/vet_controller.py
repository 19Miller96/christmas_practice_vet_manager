from Flask import Flask, render_template, request, redirect
from Flask import blueprint

from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal
import repositories.vet_repository as vet

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>")
def show(id):
    vet = vet_repository.select(id)
    animals = vet_repository.animals(vet)
    return render_template("vets/show.html", vet = vet, animals = animals)

@vets_blueprint.route("/vets/new")
def new_vet():
    animals = animal_repository.select_all()
    return render_template("vets/new.html", animals = animals)
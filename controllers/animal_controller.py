from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", animals = animals)

@animals_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    vets = animal_repository.vets(animal)
    return render_template("animals/show.html", animal = animal, vets = vets)

@animals_blueprint.route("/animals/new")
def new_animal():
    vets = vet_repository.select_all()
    return render_template("animals/new.html", vets = vets)

@animals_blueprint.route("/animals",  methods=['POST'])
def create_animal():
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    type = request.form["type"]
    owner_info = request.form["owner_info"]
    treatment_notes = request.form["treatment_notes"]
    new_animal = Animal(name, date_of_birth, type, owner_info, treatment_notes)
    animal_repository.save(new_animal)
    return redirect('/animals')

@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')
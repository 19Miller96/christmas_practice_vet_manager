from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

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

@vets_blueprint.route("/vets/<id>/animals")
def animal_list(id):
    animals = vet_repository.animals(id)
    return render_template("vets/animals.html", animals = animals)

@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html")

@vets_blueprint.route("/vets",  methods=['POST'])
def create_vet():
    name = request.form["name"]
    age = request.form["age"]
    new_vet = Vet(name, age)
    vet_repository.save(new_vet)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')

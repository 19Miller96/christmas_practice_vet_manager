from Flask import Flask, render_template, request, redirect
from Flask import blueprint

from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal
import repositories.vet_repository as vet

vets_blueprint = Blueprint("vets", __name__)
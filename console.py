import pdb
from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animal_repository.delete_all()
vet_repository.delete_all()

vet_1 = Vet('Jonathan Miller', 24)
vet_repository.save(vet_1)

animal_1 = Animal('Dougal Miller', '12th August 1996', "dog", "Susan Boyle", "Broken leg")
animal_repository.save(animal_1)
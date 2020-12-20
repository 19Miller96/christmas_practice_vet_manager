import unittest

from models.animal import Animal
from models.vet import Vet

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal_1 = Animal("Dougal Miller", "14th August 1996", "Dog", "Susan Boyle", "Broken Leg")

    def test_animal_name(self):
        self.assertEqual("Dougal Miller", self.animal_1.name)

    def test_animal_date_of_birth(self):
        self.assertEqual("14th August 1996", self.animal_1.date_of_birth)

    def test_animal_type(self):
        self.assertEqual("Dog", self.animal_1.type)
    
    def test_animal_owner_info(self):
        self.assertEqual("Susan Boyle", self.animal_1.owner_info)

    def test_animal_treatment_notes(self):
        self.assertEqual("Broken Leg", self.animal_1.treatment_notes)


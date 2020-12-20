import unittest

from models.animal import Animal
from models.vet import Vet

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal_1 = Animal("Dougal Miller", "14th August 1996", "Dog", "Susan Boyle", "Broken Leg")

    def test_animal_name(self):
        self.assertEqual("Dougal Miller", self.animal_1.name)

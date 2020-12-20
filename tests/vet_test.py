import unittest

from models.animal import Animal
from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet_1 = Vet("Jonathan Miller", 24)

    def test_name_returns(self):
        self.assertEqual("Jonathan Miller", self.vet_1.name)


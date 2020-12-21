import unittest

from tests.animal_test import TestAnimal
from tests.vet_test import TestVet

if __name__ == "__main__":
    unittest.main()

# psql -d shop_inventory -f db/shop_inventory.sql
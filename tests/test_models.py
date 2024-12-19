# tests/test_models.py
import unittest
from models import Product
from factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()

    def test_read_product(self):
        self.assertIsNotNone(self.product)

    def test_update_product(self):
        old_name = self.product.name
        self.product.name = "NewName"
        self.assertNotEqual(self.product.name, old_name)

    def test_delete_product(self):
        product_id = self.product.id
        self.product.delete()
        self.assertIsNone(Product.find(product_id))

    def test_list_all_products(self):
        products = Product.all()
        self.assertGreater(len(products), 0)

    def test_find_by_name(self):
        product = Product.find_by_name(self.product.name)
        self.assertIsNotNone(product)

    def test_find_by_category(self):
        products = Product.find_by_category(self.product.category)
        self.assertGreater(len(products), 0)

    def test_find_by_availability(self):
        products = Product.find_by_availability(self.product.available)
        self.assertGreater(len(products), 0)

if __name__ == '__main__':
    unittest.main()
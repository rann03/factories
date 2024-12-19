# tests/test_routes.py
import unittest
from flask import Flask
from routes import app
from factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.product = ProductFactory()

    def test_read_product(self):
        response = self.app.get(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        response = self.app.put(f'/products/{self.product.id}', json={"name": "UpdatedName"})
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response = self.app.delete(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 204)

    def test_list_all_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_list_by_name(self):
        response = self.app.get(f'/products?name={self.product.name}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_category(self):
        response = self.app.get(f'/products?category={self.product.category}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_availability(self):
        response = self.app.get(f'/products?available={self.product.available}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
# tests/factories.py
from factory import Factory, Faker
from models import Product

class ProductFactory(Factory):
    class Meta:
        model = Product

    id = Faker('uuid4')
    name = Faker('word')
    category = Faker('word')
    available = Faker('boolean')
    price = Faker('random_number', digits=5)
# features/steps/load_steps.py
from behave import given
from factories import ProductFactory

@given('the following products')
def step_impl(context):
    for row in context.table:
        ProductFactory(name=row['name'], category=row['category'], available=row['available'], price=row['price'])
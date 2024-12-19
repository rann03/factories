# service/routes.py
from flask import Flask, jsonify, request
from models import Product

app = Flask(__name__)

@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.find(id)
    return jsonify(product.serialize())

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.find(id)
    product.update(data)
    return jsonify(product.serialize())

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.find(id)
    product.delete()
    return '', 204

@app.route('/products', methods=['GET'])
def list_all_products():
    products = Product.all()
    return jsonify([product.serialize() for product in products])

@app.route('/products', methods=['GET'])
def list_by_name():
    name = request.args.get('name')
    products = Product.find_by_name(name)
    return jsonify([product.serialize() for product in products])

@app.route('/products', methods=['GET'])
def list_by_category():
    category = request.args.get('category')
    products = Product.find_by_category(category)
    return jsonify([product.serialize() for product in products])

@app.route('/products', methods=['GET'])
def list_by_availability():
    available = request.args.get('available')
    products = Product.find_by_availability(available)
    return jsonify([product.serialize() for product in products])

if __name__ == '__main__':
    app.run(debug=True)
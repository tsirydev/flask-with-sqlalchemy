# wsgi.py
# pylint: disable=missing-docstring

#import os
#import logging
#logging.warn(os.environ["DUMMY"])

BASE_URL = '/api/v1'

from flask import Flask
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

# [...] After `db = SQLAlchemy(app)`
from models import Product

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200
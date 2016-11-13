import json

import requests
from pymongo import MongoClient
from pymongo import errors
from bson import json_util
from bson import ObjectId

MONGO_URI = 'mongodb://localhost:27017/'
url = 'http://redsky.target.com/v1/pdp/tcin/13860428?excludes=taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics'


def get_db():
    try:
        client = MongoClient(MONGO_URI + 'myRetail')
        db = client.myRetail
        return db
    except errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: {}".format(e)


def list_dbs():
    client = MongoClient(MONGO_URI)
    return client.database_names()


def add_products(db):
    try:
        response = requests.get(url)
        obj = json.loads(response.content)
        db.products.insert(obj)
    except requests.exceptions.RequestException as e:
        print("Error: Invalid URL{}".format(e))
    except errors.DuplicateKeyError as e:
        print("duplicate Values in database: {}".format(e))
    except ValueError as e:
        print("Database insert error: {}".format(e))


def delete_products(db):
    db.products.drop()


def get_raw_products(db):
    for product in db.products.find():
        return product
        #print product.encode('utf-8')


def get_ascii_products(db):
    obj = db.products.find()
    products = list(obj)
    #json serializing mongoddb
    rs = json.dumps(products, default=json_util.default)
    return rs


def get_product_id(db):
    # list comprehension
    #products = [p for p in db.products.find({"product.available_to_promise_network.product_id": 13860428})]
    product_id = [p for p in db.products.find({"product.item.tcin": "13860428"})]
    for p in db.products.find({"product.item.tcin": "13860428"}):
        print p
    return product_id


if __name__ == "__main__":
    db = get_db()
    #delete_products(db)
    #add_products(db)
    print(list_dbs())
    #print(get_ascii_products(db))
    #print(get_raw_products(db))
    get_product_id(db)


import json

import requests
from pymongo import MongoClient
from pymongo import errors
from bson import json_util
from bson import ObjectId


url = 'http://redsky.target.com/v1/pdp/tcin/13860428?excludes=taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics'


def get_db():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.myRetail
        return db
    except errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e


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


def get_raw_products(db):
    for product in db.products.find():
        return product
        #print product.encode('utf-8')


def get_ascii_products(db):
    obj = db.products.find().limit(1)
    products = list(obj)
    #json serializing mongoddb
    rs = json.dumps(products, default=json_util.default)
    return rs


def get_one_product(db):
    #db.products.find(ObjectId('5826aa1df1c545b0740a7205'))
    
    # num = db.products.find({"is_po_box_prohibited": "true"}).count()
    # obj = db.products.find({"_id": ObjectId("5826aa1df1c545b0740a7205")})
    # stuff = list(db.products.find({"_id": ObjectId("5826aa1df1c545b0740a7205")}))
    # print(stuff, num)

    for product in db.products.find({"product.item.fulfillment.is_po_box_prohibited": True}):
        print product

def delete_products(db):
    db.products.drop()

if __name__ == "__main__":
    db = get_db()
    #delete_products(db)
    #add_products(db)
    #print(get_ascii_products(db))
    #print(get_raw_products(db))
    get_one_product(db)


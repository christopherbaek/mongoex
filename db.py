from pymongo import MongoClient


#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------
MONGO_URI = 'mongodb://localhost:27017/'




def get_products_collection():
    client = MongoClient(MONGO_URI)
    db = client.retail
    return db.products


def insert_product_data(product_data):
    products_collection = get_products_collection()
    products_collection.insert_one(product_data)


def retrieve_all_products():
    products_collection = get_products_collection()
    return [p for p in products_collection.find()]


def retrieve_product_by_id(id):
    products_collection = get_products_collection()
    return products_collection.find_one({'product.available_to_promise_network.product_id': id})


def drop_products_collection():
    products_collection = get_products_collection()
    products_collection.drop()

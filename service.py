import db
from db import retrieve_all_products, retrieve_product_by_id


def retrieve_all_products():
    products = db.retrieve_all_products()

    # add business logic here

    return products


def retrieve_product_by_id(id):
    product = db.retrieve_product_by_id(id)

    # add business logic here

    return product


import db
from db import retrieve_all_products, retrieve_product_by_id


def retrieve_all_products():
    products = db.retrieve_all_products()

    # add business logic here

    return products


def retrieve_all_products_as_dict():
    products = retrieve_all_products()

    # product_dict = {}
    # 
    # for p in products:
    #     product_id = p['product']['available_to_promise_network']['product_id']
    #     product_dict[product_id] = p
    #
    # return product_dict

    return {p['product']['available_to_promise_network']['product_id']:p for p in products}


def retrieve_product_by_id(id):
    product = db.retrieve_product_by_id(id)

    # add business logic here

    return product


def retrieve_simplified_products():
    products = retrieve_all_products()
    return [extract_id_and_title(p) for p in products]


def extract_id_and_title(product):
    """
    Given product data, returns a dictionary with only the id and title
    """
    id = product['product']['available_to_promise_network']['product_id']
    title = product['product']['item']['product_description']['title']
    return {'id': id, 'title': title}

def retrieve_item_by_product_id(id):
    product = retrieve_product_by_id(id)
    return product['product']['item']

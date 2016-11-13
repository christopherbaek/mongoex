import argparse
import requests
import sys

from db import insert_product_data, retrieve_all_products, drop_products_collection


#-------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------
TEST_DATA_URL = 'http://redsky.target.com/v1/pdp/tcin/13860428?excludes=taxonomy,price,promotion,bulk_ship,rating_and_review_reviews,rating_and_review_statistics,question_answer_statistics'




def retrieve_test_data():
    response = requests.get(TEST_DATA_URL)

    return response.json()

def load():
    insert_product_data(retrieve_test_data())


def print_all():
	for product_data in retrieve_all_products():
		print product_data


def drop():
	drop_products_collection();


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('COMMAND', choices=('LOAD','PRINT_ALL', 'DROP'))

    args = parser.parse_args(argv)

    if args.COMMAND == 'LOAD':
        load()
    elif args.COMMAND == 'PRINT_ALL':
        print_all()
    elif args.COMMAND == 'DROP':
    	drop()
    else:
        print 'Unknown command:', args.COMMAND


if __name__ == '__main__':
    main(sys.argv[1:])

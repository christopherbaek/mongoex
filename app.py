from flask import Flask
from flask import jsonify
from pymongo import MongoClient

# the Flask application
app = Flask(__name__)

# Mongo DB
client = MongoClient('mongodb://localhost:27017/')
db = client.myRetail


@app.route('/')
def index():
	# run Mongo query
	products = [p for p in db.products.find({"product.item.fulfillment.is_po_box_prohibited": True})]
	response_body = {'products': products}
	return jsonify(**response_body)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

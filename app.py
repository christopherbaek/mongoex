from flask import Flask
from flask import jsonify
from pymongo import MongoClient

# the Flask application
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'myRetail'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/myRetail'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
	# run Mongo query
	products = [p for p in mongo.db.products.find({"product.item.fulfillment.is_po_box_prohibited": True})]
	response_body = {'products': products}
	return jsonify(**response_body)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

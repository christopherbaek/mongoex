from bson import json_util
from flask import Flask, Response, render_template

from service import retrieve_all_products, retrieve_product_by_id


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    products = retrieve_all_products()
    return render_template('products.html', products=products)


@app.route('/api/v1/products/')
def api_products():
    products = retrieve_all_products()

    return Response(
        json_util.dumps({'products' : products}),
        mimetype='application/json'
    )


@app.route('/api/v1/products/<product_id>')
def api_product(product_id):
    product = retrieve_product_by_id(product_id)

    return Response(
        json_util.dumps(product),
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


from saleappv1 import app , utils
from  flask import render_template


@app.route("/")
def index ():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)

@app.route("/production")
def products_list():
    products = utils.read_data(path='data/production.json')
    return render_template('products.html',
                            products = products)


if __name__ == "__main__":
    app.run(debug = True)
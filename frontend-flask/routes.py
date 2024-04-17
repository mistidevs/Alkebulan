
#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, request
from flask import jsonify

from models import storage
from models.product import Product
import uuid
import json



app = Flask(__name__,  static_folder='static')
app.url_map.strict_slashes = False



@app.route("/home")
@app.route("/", methods=["GET"])
def home():
    """The home page"""
    products = storage.all(Product).values()
    products = sorted(products, key=lambda k: k.name)

    return render_template('home.html', products=products, cache_id=uuid.uuid4())
        

@app.route("/details", methods=['GET', 'POST'])
def details():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("details.html", cache_id=cache_id, details=details)

@app.route("/products")
def products():
    """The home page"""
    cache_id = uuid.uuid4()
    products = storage.all(Product).values()
    products = sorted(products, key=lambda k: k.created_at)
    return render_template("more-products.html", cache_id=cache_id, products=products,)

@app.route("/shop")
def shop():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("shop.html", cache_id=cache_id)

@app.route("/contact")
def contact():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("contact.html", cache_id=cache_id)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

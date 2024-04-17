
#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
import uuid



app = Flask(__name__,  static_folder='static')
app.url_map.strict_slashes = False


@app.route("/home")
@app.route("/")
def home():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("home.html", cache_id=cache_id)
        

@app.route("/details")
def details():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("details.html", cache_id=cache_id)

@app.route("/products")
def products():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("more-products.html", cache_id=cache_id)

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

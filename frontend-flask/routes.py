
#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
from models import storage
from models.product import Product
from models.farmer import Farmer
from models.farmer_product import FarmerProduct
from models.order import Order
import uuid
import json
from flask_login import LoginManager, login_user, logout_user, current_user
from hashlib import md5


app = Flask(__name__,  static_folder='static')
app.url_map.strict_slashes = False
app.config["SECRET_KEY"] = "djfwfwm5kl4nfpnwfknw5n5nslk"

login_manager = LoginManager()
login_manager.init_app(app)


def redirect_back(default='/', **kwargs):
    return redirect(request.referrer or url_for(default, **kwargs))

@app.teardown_appcontext
def close_db(error):
    from models import storage
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()

@login_manager.user_loader
def load_user(user_id):
    """
    Loads a user from memory
    """
    from models.consumer import Consumer
    from models import storage
    consumers = storage.all(Consumer)
    for key, value in consumers.items():
        if value.id == user_id:
            return value

@app.route('/register', methods=["GET", "POST"], strict_slashes=False)
def register():
    from models.consumer import Consumer
    #from models.farmer import Farmer
    from models import storage
    """
    Creates a new user from the frontend interface
    """
    required_fields = ["user_name", "password", "full_name", "email", "phone_number"]
    if request.method == "POST":
        missing_fields = []
        for field in required_fields:
            if request.form.get(field) == "":
                missing_fields.append(field)

        print(missing_fields)
        
        if missing_fields:
            error_message = f"Please provide the following missing fileds: {', '.join(missing_fields)}"
            return render_template("signup.html", error_message=error_message)
        
        print(request.form.get("role"))
        
        if request.form.get("role") == "consumer":
            consumer = Consumer(user_name=request.form.get("user_name"),
                                password=request.form.get("password"),
                                full_name=request.form.get("full_name"),
                                email=request.form.get("email"),
                                phone_number=request.form.get("phone_number"))
            print(consumer)
            storage.new(consumer)
        elif request.form.get("role") == "Farmer":
            pass
        storage.save()
        storage.close()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """
    Offers a user an opportunity to log in
    """
    from models.consumer import Consumer
    from models import storage
    from models.valid_login import ValidLogin
    from models.invalid_login import InvalidLogin

    required_fields = ["user_name", "password"]
    if request.method == "POST":
        flag = 0
        missing_fields = []
        for field in required_fields:
            if request.form.get(field) is None:
                missing_fields.append(field)
        
        if missing_fields:
            error_message = f"Please provide the following missing fileds: {', '.join(missing_fields)}"
            return render_template("login.html", error_message=error_message)
        
        consumers = storage.all(Consumer)
        for key, value in consumers.items():
            print(request.form.get("user_name"))
            if value.user_name == request.form.get("user_name"):
                flag = 1
                print("The user is found")
                consumer = storage.get(Consumer, value.id)
                input_password = md5(request.form.get("password").encode()).hexdigest()
                if consumer.password == input_password:
                    login_user(consumer)
                    valid_login = ValidLogin(user_name=request.form.get("user_name"))
                    storage.new(valid_login)
                    storage.save()
                    storage.close()
                    return redirect(url_for("home"))
                else:
                    print(request.form.get("password"))
                    print("This password is wrong")
                    invalid_login = InvalidLogin(user_name=request.form.get("user_name"),
                                                 password=request.form.get("password"),
                                                 reason="Wrong password")
                    storage.new(invalid_login)
                    storage.save()
                    storage.close()
                    error_wrong_password = f"Wrong password"
                    return render_template("login.html", error_message=error_wrong_password)
        if flag == 0:
            print("This user does not exist")
            invalid_login = InvalidLogin(user_name=request.form.get("user_name"),
                                            password=request.form.get("password"),
                                            reason="User does not exist")
            storage.new(invalid_login)
            storage.save()
            storage.close()
            error_no_user = f"This user does not exist"
            return render_template("login.html", error_message=error_no_user)
    return render_template("login.html")
        
@app.route("/logout")
def logout():
    """
    Logs a user out
    """
    logout_user()
    return redirect(url_for("home"))

@app.route("/order/<farmer_product_id>", methods=["POST"], strict_slashes=False)
def order(farmer_product_id):
    """
    Ordering a product from a farmer
    """
    from models import storage
    from models.farmer_product import FarmerProduct
    from models.order import Order
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    farmer_product = storage.get(FarmerProduct, farmer_product_id)
    print(current_user.id)
    order = Order(consumer_id=current_user.id,
                    farmer_id=farmer_product.farmer_id,
                    product_id=farmer_product.product_id,
                    unit_price=farmer_product.price,
                    quantity=1,
                    total_price=int(farmer_product.price) * 1)
    storage.new(order)
    storage.save()
    storage.close()
    return redirect_back()

@app.route("/home")
@app.route("/", methods=["GET"])
def home():
    """The home page"""
    farmer_products = storage.all(FarmerProduct).values()
    for farmer_product in farmer_products:
        product = storage.get(Product, farmer_product.product_id)
        farmer = storage.get(Farmer, farmer_product.farmer_id)
        farmer_product.picture = product.picture
        farmer_product.farmer_picture = farmer.picture
        farmer_product.name = product.name
    products = sorted(farmer_products, key=lambda k: k.name)

    return render_template('home.html', products=products, cache_id=uuid.uuid4())
        

@app.route("/details/<farmer_product_id>", methods=['GET', 'POST'])
def details(farmer_product_id):
    """The home page"""
    cache_id = uuid.uuid4()
    farmer_products = [farmer_product for farmer_product in storage.all(FarmerProduct).values() if farmer_product.id != farmer_product_id]
    for farmer_product in farmer_products:
        product = storage.get(Product, farmer_product.product_id)
        farmer = storage.get(Farmer, farmer_product.farmer_id)
        farmer_product.picture = product.picture
        farmer_product.farmer_picture = farmer.picture
        farmer_product.name = product.name
    products = sorted(farmer_products, key=lambda k: k.name)
    
    details = storage.get(FarmerProduct, farmer_product_id)
    product = storage.get(Product, details.product_id)
    farmer = storage.get(Farmer, details.farmer_id)
    details.picture = product.picture
    details.farmer_picture = farmer.picture
    details.name = product.name
    details.description = product.description
    
    return render_template("details.html", cache_id=cache_id, details=details, products=products)

@app.route("/products")
def products():
    """The home page"""
    cache_id = uuid.uuid4()
    farmer_products = storage.all(FarmerProduct).values()
    for farmer_product in farmer_products:
        product = storage.get(Product, farmer_product.product_id)
        farmer = storage.get(Farmer, farmer_product.farmer_id)
        farmer_product.picture = product.picture
        farmer_product.farmer_picture = farmer.picture
        farmer_product.name = product.name
    products = sorted(farmer_products, key=lambda k: k.created_at)
    return render_template("more-products.html", cache_id=cache_id, products=products,)

@app.route("/shop", methods=['GET', 'POST'])
def shop():
    """The home page"""
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    cache_id = uuid.uuid4()
    orders = [order for order in storage.all(Order).values() if order.consumer_id == current_user.id and order.in_cart == True]
    for order in orders:
        product = storage.get(Product, order.product_id)
        farmer = storage.get(Farmer, order.farmer_id)
        order.picture = product.picture
        order.farmer_picture = farmer.picture
        order.name = product.name
    return render_template("shop.html", cache_id=cache_id, orders=orders)

@app.route("/contact")
def contact():
    """The home page"""
    cache_id = uuid.uuid4()
    return render_template("contact.html", cache_id=cache_id)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
""" Starts a Flash Web Application """
from os import environ
from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, login_user, logout_user
from hashlib import md5


app = Flask(__name__)
app.config["SECRET_KEY"] = "djfwfwm5kl4nfpnwfknw5n5nslk"

login_manager = LoginManager()
login_manager.init_app(app)


@app.teardown_appcontext
def close_db(error):
    from models import storage
    """ Remove the current SQLAlchemy Session """
    storage.close()

@login_manager.user_loader
def loader_user(user_id):
    """Loads a user from memory"""
    from models.consumer import Consumer
    from models import storage
    consumers = storage.all(Consumer)
    for key, value in consumers.items():
        if value.id == user_id:
            return value

@app.route('/register', methods=["GET", "POST"], strict_slashes=False)
def register():
    from models.consumer import Consumer
    from models import storage
    """Creates a new user from the frontend interface"""
    if request.method == "POST":
        consumer = Consumer(user_name=request.form.get("user_name"),
                            password=request.form.get("password"),
                            full_name=request.form.get("full_name"),
                            email=request.form.get("email"),
                            phone_number=request.form.get("phone_number"))
        storage.new(consumer)
        storage.save()
        storage.close()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Offers a user an opportunity to log in"""
    from models.consumer import Consumer
    from models import storage
    if request.method == "POST":
        consumers = storage.all(Consumer)
        for key, value in consumers.items():
            print(request.form.get("user_name"))
            if value.user_name == request.form.get("user_name"):
                consumer = storage.get(Consumer, value.id)
                print(consumer)
                print(consumer.password)
                input_password = md5(request.form.get("password").encode()).hexdigest()
                print(input_password)
                if consumer.password == input_password:
                    login_user(consumer)
                    return redirect(url_for("home"))
    return render_template("login.html")
        
@app.route("/logout")
def logout():
    """Logs a user out"""
    logout_user()
    return redirect(url_for("home"))

@app.route("/")
def home():
    """The home page"""
    return render_template("home.html")
        

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
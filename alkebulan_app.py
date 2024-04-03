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
    required_fields = ["user_name", "password", "full_name", "email", "phone_number"]
    if request.method == "POST":
        missing_fields = []
        for field in required_fields:
            if request.form.get(field) is None:
                missing_fields.append(field)
        
        if missing_fields:
            error_message = f"Please provide the following missing fileds: {', '.join(missing_fields)}"
            return render_template("signup.html", error_message=error_message)
        
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
    from models.valid_login import ValidLogin
    from models.invalid_login import InvalidLogin

    required_fields = ["user_name", "password"]
    if request.method == "POST":
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
                    invalid_login = InvalidLogin(user_name=request.form.get("user_name"),
                                                 password=input_password)
                    storage.new(invalid_login)
                    storage.save()
                    storage.close()
                    error_wrong_password = f"Wrong password"
                    return render_template("login.html", error_message=error_wrong_password)
            else:
                invalid_login = InvalidLogin(user_name=request.form.get("user_name"),
                                             password="None")
                storage.new(invalid_login)
                storage.save()
                storage.close()
                error_no_user = f"This user does not exist"
                return render_template("login.html", error_message=error_no_user)
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
from flask import Flask, redirect, request, render_template, url_for
from login_logic import login_manager, LoginHandler, PasswordHashing
from db_Model import User, db
from user_service import UserService

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
login_manager.init_app(app)
user_service = UserService()
db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        success = user_service.create_user(request.form)
        return redirect(url_for("secrets.html")) if success else redirect(url_for("home"))
    return render_template("register.html")



@app.route("/logout")
def logout():
    return render_template("")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

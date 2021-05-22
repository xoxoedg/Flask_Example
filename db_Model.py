from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import request


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))

    def __init__(self):
        self.username = request.form.get("name")
        self.password = request.form.get("password")
        self.email = request.form.get("email")


    def safe_new_user_in_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_user_in_db(self):
        db.session.delete(self)
        db.session.commit()


class UserService:

    def create_user(self, form):
        return User()

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import request


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))

    def __init__(self, registration_form):
        self.username = registration_form["username"]
        self.email = registration_form["email"]
        self.password = registration_form["password"]

    def safe_new_user_in_db(self):
        already_signed_in = self.login_handler.check_user_already_signed_in(user_email=self.email)
        correct_email = self._has_correct_pattern(self.email)

        if not already_signed_in and correct_email:
            db.session.add(self)
            db.session.commit()
            return True
        return False

    def delete_user_in_db(self):
        db.session.delete(self)
        db.session.commit()

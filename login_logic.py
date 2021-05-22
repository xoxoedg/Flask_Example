from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from db_Model import User, db
from flask import app

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class PasswordHashing:

    def hash_password(self, password):
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        return hashed_password

    def check_hashed_password(self, hash_password, typed_password):
        check_password = check_password_hash(hash_password, typed_password)
        return check_password

class LoginHandler:

    def check_user_already_signed_in(self, user_email):
        already_exists = User.query.filter_by(email=user_email).first()
        if already_exists:
            print("Sorry you are already signed in. Try login in!")
            return True
        else:
            return False

    def log_out_user(self):
        return logout_user()

    def authenticated(self, user):
        user = current_user()
        return user.is_authenticated

    def check_if_user_is_signed_in(self, email_db, user):
        if email_db:
            flash_message = "Youve already signed up, log in instead"
            return flash_message
        else:
            db.session.add(user)
            db.session.commit()
            return self.log_in_user(user)

    # def log_in_user(self, email, user_password):
    #     new_user_hashed_password = PasswordHashing()
    #
    #     if new_user:
    #         if user_password.check_hashed_password():
    #             return login_user(user)
    #         return "Sorry wrong password"
    #     return "You are not registered"

from db_Model import User
from login_logic import PasswordHashing, LoginHandler


class UserService:

    def __init__(self):
        self.pw_hashing = PasswordHashing()
        self.login_handler = LoginHandler()

    def create_user(self, form):
        already_signed_in = self.login_handler.check_user_already_signed_in(user_email=form.email)
        correct_email = self._has_correct_pattern(form.email)

        if not already_signed_in and correct_email:
            new_user = self._populate_form_data(form)
            new_user.safe_new_user_in_db()
            return True

        return False

    def _populate_form_data(self, form):
        new_user = User()
        new_user.username = form["username"]
        new_user.password = self.pw_hashing.hash_password(form["password"])
        new_user.email = form["email"]
        return new_user

    def _has_correct_pattern(self, email: str):
        splitted_at_at = email.split("@")
        return len(splitted_at_at) == 2
from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        name_regex = re.compile("^[a-z]{3,}$")
        if not name_regex.match(username):
            raise AuthenticationError("Invalid username")

        pw_negative_regex = re.compile("^(.{0,7}|[^0-9]*|[^a-z]*)$")
        if pw_negative_regex.match(password):
            raise AuthenticationError("Invalid password")

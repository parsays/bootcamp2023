import json
import re


class ValidationError(ValueError):
    pass


class User:
    def __init__(self, name, email, password, gift_code):
        self.name = name
        self.email = email
        self.password = password
        self.gift_code = gift_code

    def updade_gift_code(self, gift_code):
        self.gift_code = gift_code

    @property
    def name(self) -> str:
        return self.__username

    @name.setter
    def name(self, value: str) -> None:
        if not re.match('[a-zA-Z]{3,}', value):
            raise ValidationError("Invalid username!")
        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        if not re.match('[a-zA-Z0-9]{8,}', value):
            raise ValidationError("Invalid password!")
        self.__password = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError('Email must be a string')
        if not value.endswith('@gmail.com'):
            raise ValidationError('Invalid email format')
        self.__email = value


class UserDatabase:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            with open(self.filename, 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'w') as f:
            json.dump(self.users, f)

    def add_user(self, user):
        self.users.append({
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'gift_code': user.gift_code,
            })

    def update_user_gift_code(self, email, gift_code):
        for user in self.users:
            if user['email'] == email:
                user_obj = User(
                    user['name'],
                    user['email'],
                    user['password'],
                    user['gift_code']
                )
                user_obj.updade_gift_code(gift_code)
                user['gift_code'] = gift_code
                break
        else:
            raise ValueError(f'User with email {email} not found')

    def get_user(self, email):
        for user in self.users:
            if user['email'] == email:
                return User(
                    user['name'],
                    user['email'],
                    user['password'],
                    user['gift_code']
                    )
        return None

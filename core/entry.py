import os
from getpass import getpass
import json
import re
import logging

logger = logging.getLogger(__name__)


class ValidationError(ValueError):
    pass


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

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
            'password': user.password
            })

    def get_user(self, email):
        for user in self.users:
            if user['email'] == email:
                return User(user['name'], user['email'], user['password'])
        return None


def clear_screen():
    # Clear the screen for Windows-based systems
    if os.name == 'nt':
        os.system('cls')
    # Clear the screen for Unix/Linux/Mac-based systems
    else:
        os.system('clear')


def entry():
    signed_in = False
    while not signed_in:
        clear_screen()
        print('WELCOME TO OUR ONLINE MOBILE SHOP')
        command = input('Press signup, signin: ').lower()
        if command == 'signup':
            with UserDatabase('users.json') as user_db:
                name = input('Name: ')
                email = input('Email: ')
                password = input('Password: ')
                user = User(name, email, password)
                user_db.add_user(user)
                getpass('signup successfully')
        if command == 'signin':
            with UserDatabase('users.json') as user_db:
                email = input('Email: ')
                password = input('Password: ')
                user = user_db.get_user(email)
                if user is not None and user.password == password:
                    getpass('Login successful!')
                    signed_in = True
                else:
                    getpass('Incorrect email or password.')
    return name

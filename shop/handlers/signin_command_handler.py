import logging
from models.user import UserDatabase
from getpass import getpass

logger = logging.getLogger(__name__)


def handel_signin_command():
    logger.info('A user want to sign in.')
    with UserDatabase('users.json') as user_db:
        email = input('Email: ')
        password = input('Password: ')
        user = user_db.get_user(email)
        if user is not None and user.password == password:
            logger.info(f'{user.name} logged in successfully.')
            getpass('Login successful!')
            return user
        else:
            logger.warning('While user signing in input wrong info.')
            getpass('Incorrect email or password.')
            return None

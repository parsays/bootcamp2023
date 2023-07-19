import logging
from models.user import User, UserDatabase, ValidationError
from getpass import getpass

logger = logging.getLogger(__name__)


def handel_signup_command():
    logger.info('A user want to sign up.')
    with UserDatabase('users.json') as user_db:
        try:
            name = input('Name: ')
            email = input('Email: ')
            password = input('Password: ')
            user = User(name, email, password, gift_code=None)
            logger.info(f'{user.name} validated successfully.')
        except ValidationError as msg:
            logger.warning(f'User validated unsuccessfully - {msg}.')
            print(msg)
            getpass()
            return
        user_db.add_user(user)
        logger.info(f'{user.name} sign up successfully.')
        getpass('signup successfully.')
        return None

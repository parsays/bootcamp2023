import logging
import os
from getpass import getpass
from models.user import User, ValidationError

logger = logging.getLogger(__name__)


def clear_screen():
    # Clear the screen for Windows-based systems
    if os.name == 'nt':
        os.system('cls')
    # Clear the screen for Unix/Linux/Mac-based systems
    else:
        os.system('clear')


def handle_signin_command(username: str, password: str, users: dict) -> bool:
    logger.info(f'{username} wants to login')
    try:
        user = User(username, password)
        logger.info(f'{username} validated successfully')
    except ValidationError as msg:
        print(msg)
        logger.warning(f'{username} was not validated.')
        getpass('Press enter to continue...')
    if user.signin(username, password, users):
        clear_screen()
        print('You signed in succesfully')
        logger.info(f'{username} - {password} logged in successfully')
        getpass('')
        signed_in = True
        return signed_in
    else:
        clear_screen()
        logger.warning(f'{username} - {password} user or pass incorrect')
        print('username/password incorrect')
        getpass('')
        signed_in = False
        return signed_in

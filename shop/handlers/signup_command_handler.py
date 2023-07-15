import logging
import os
from getpass import getpass
from models.user import  User, ValidationError

logger= logging.getLogger(__name__)

def clear_screen():
    # Clear the screen for Windows-based systems
    if os.name == 'nt':
        os.system('cls')
    # Clear the screen for Unix/Linux/Mac-based systems
    else:
        os.system('clear')



def handle_signup_command(username, password: str, users: dict):
    logger.info(f'{username} wants to signup')
    fullname= input('Input your fullname: ')
    email= input('Input your Email: ')
    try:
        try:
            user= User(username, password)
            logger.info(f'{username} validated successfully')
        except ValidationError as msg:
            print(msg)
            logger.warning(f'{username} was not validated')
            getpass('Press enter to continue...')
        user.signup(fullname, username, password, email, users)
        clear_screen()
        print('You signup successfully. Please enter to signin')
        getpass('')
    except Exception as msg:
        print(msg)
        logger.warning(f'{username} NOTEMPLIMENTED')
        getpass('')

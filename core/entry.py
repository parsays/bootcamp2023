import os
from getpass import getpass
import logging
from models.command import ENTERY_COMMANDS


logger = logging.getLogger(__name__)


def clear_screen():
    # Clear the screen for Windows-based systems
    if os.name == 'nt':
        os.system('cls')
    # Clear the screen for Unix/Linux/Mac-based systems
    else:
        os.system('clear')


def entry():
    signed_in = False
    logger.info('A user enter the shop.')
    while not signed_in:
        clear_screen()
        print('WELCOME TO OUR ONLINE MOBILE SHOP')
        command = input('Press signup, signin: ').lower()
        if command in ENTERY_COMMANDS:
            execute_action = ENTERY_COMMANDS[command]
            signed_in = execute_action()
        else:
            logger.warning('User input wrong command.')
            print('dear enunimious!! You have input WRONG command.')
            getpass('Please enter to continue...')
    return signed_in

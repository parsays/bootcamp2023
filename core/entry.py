import os
from getpass import getpass
from models.command import ENTERY_COMMANDS


def clear_screen():
    # Clear the screen for Windows-based systems
    if os.name == 'nt':
        os.system('cls')
    # Clear the screen for Unix/Linux/Mac-based systems
    else:
        os.system('clear')


def entry():
    users = {
        'Parsa': {
            'fullname': 'parsa',
            'password': 'Parsa6666',
            'email': 'parsa.ys10@gmail.com'
            },
        'user2': {
            'fullname': 'pourya',
            'password': 'user2',
            'email': 'user2@gmail.com'
            }
    }

    signed_in = False
    while not signed_in:
        clear_screen()
        print('WELCOME TO OUR ONLINE MOBILE SHOP')
        username = input('username(note: capital and lower char): ')
        password = getpass('password(note: capital/lower and numers): ')
        clear_screen()
        try:
            command = input('Press signup, signin: ')
            if command in ENTERY_COMMANDS:
                execute_action = ENTERY_COMMANDS[command]
                signed_in = execute_action(username, password, users)
        except Exception as msg:
            print(f'An error accured: {msg}')
    return username

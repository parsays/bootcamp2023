import logging
from models.basket import Basket, clear_screen
from shop.helpers.consts import EXIT_COMMANDS, RUNNING
from conf import *
from shop.handlers.add_command_handler import handel_add_command
from getpass import getpass


logger= logging.getLogger(__name__)


def handel_remove_command(store_list: list, store: dict, basket: list, username):
    print(basket)
    if basket== list():
        logger.warning(f' wanted to remove item from his/her empty list')
        status= input('WARNING: Your basket is empty. You want to add a gadget?[Y/N]>> ').lower()
        clear_screen()
        if status == 'y':
            logger.info(f'{username} wants to add item from remove section')
            handel_add_command(store_list, store, basket, username)
        elif status == 'n':
            logger.info(f'{username} backed to the main')
            return
        else:
            logger.warning(f'{username} input unrelated command')
            print('Dear {username}!! You input unrelated command')
            getpass('press enter to continue>>> ')
            return


    item= input('Remove gadget or press EXIT COMMANDS>> ').lower()
    if item in EXIT_COMMANDS:
        logger.info(f'{username} exit from removing option')
        clear_screen()

    b= Basket(username)
    removeable=b.remove_products(basket, item)

    if removeable:
        print(f'Dear {username} {item} removed successfully')
        logger.info(f'{username} removed {item} successfully')
    else:
        logger.warning(f'{username} input unrelated gadget')
        print(f'Dear {username} {item} is not in your basket.')
        getpass('Press enter to continue>> ')
        clear_screen()
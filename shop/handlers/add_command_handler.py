import logging
from models.basket import Basket, clear_screen
from shop.helpers.consts import EXIT_COMMANDS, RUNNING
from conf import *

logger= logging.getLogger(__name__)

def handel_add_command(store_list: list, store: dict, basket: list, username):
    logger.info(f'{username} wants to add an item to basket')
    while RUNNING:
        print(list(store['smart_phone']))
        brand= input('Add brand or press EXIT COMMANDS >> ').lower()
        if brand in EXIT_COMMANDS:
            logger.info(f'{username} exit from adding section')
            clear_screen()
            break
        try:
            store['smart_phone'][brand]
            print(list(store['smart_phone'][brand]))
            model= input('Add model>> ').lower()
            clear_screen()
            try:
                store['smart_phone'][brand][model]
                number= int(input('How many>> '))
                b = Basket(username)
                basket=  b.add_products(basket, brand, model, number)
                logger.info(f'{username} add {brand} - {model} to the basket')
                print(f'Dear {username} your gadget {brand} - {model} added successfully.')
                input('Please press enter to continue>> ')
                clear_screen()
            except KeyError:
                logger.warning(f'{username} wants to add {brand} - {model} which is unavailable')
                print(f'Dear {username}! we do not have {brand} - {model} in our store.')
                input('Please press enter to continue>> ')
                clear_screen()
        except KeyError:
            logger.warning(f'{username} wants to add {brand} brand which is unavailable')
            print(f'Dear {username}! we do not have {brand} brand in our store.')
            input('Please press enter to continue>> ')
            clear_screen()
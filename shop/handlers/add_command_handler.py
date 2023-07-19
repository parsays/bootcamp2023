import logging
from models.basket import Basket, clear_screen
from shop.helpers.consts import EXIT_COMMANDS, RUNNING

logger = logging.getLogger(__name__)


def handel_add_command(
        store_list: list,
        store: dict,
        basket: list,
        username
        ) -> None:
    logger.info(f'{username} wants to add an item to basket')
    while RUNNING:
        print(list(store['smart_phone']))
        brand = input('Add brand or press EXIT COMMANDS >> ').lower()
        if brand in EXIT_COMMANDS:
            logger.info(f'{username} exit from adding section')
            clear_screen()
            break
        try:
            store['smart_phone'][brand]
            print(list(store['smart_phone'][brand]))
            model = input('Add model>> ').lower()
            clear_screen()
            try:
                store['smart_phone'][brand][model]
                try:
                    number = int(input('How many>> '))
                    b = Basket(username)
                    basket = b.add_products(basket, brand, model, number)
                    logger.info(f'{username} add {brand} - {model}.')
                    print(f'Dear {username} your gadget {brand} - {model} '
                          f'added successfully.')
                    input('Please press enter to continue>> ')
                except ValueError:
                    print(f'Dear {username}!! You have to input int.')
                    input('Please press enter to continue>> ')
                clear_screen()
            except KeyError:
                logger.warning(f'{username} wants to add {brand} - {model} '
                               f'which is unavailable')
                print(f'Dear {username}! we do not have {brand} - {model} '
                      f'in our store.')
                input('Please press enter to continue>> ')
                clear_screen()
        except KeyError:
            logger.warning(f'{username} wants to add {brand} '
                           f'brand which is unavailable')
            print(f'Dear {username}! we do not have {brand} in our store.')
            input('Please press enter to continue>> ')
            clear_screen()

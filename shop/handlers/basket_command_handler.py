import logging
from models.basket import Basket, clear_screen
from getpass import getpass

logger = logging.getLogger(__name__)


def handle_basket_command(
        store_list: list,
        store: dict,
        basket: list, username: str
        ) -> None:
    logger.info(f'{username} wants to check basket.')
    if basket == list():
        logger.warning(f'{username} wants to show basket from empty list')
        status = input('Basket is empty. add a gadget?[Y/N]>> ').lower()
        clear_screen()
        if status == 'y':
            logger.info(f'{username} wants to an item to basket')
            b = Basket(username)
            basket = b.show_basket(basket)
        elif status == 'n':
            logger.info(f'{username} exit show_basket section')
            clear_screen()
            return
        else:
            logger.warning(f'{username} input unrelated command')
            print(f'Dear {username}! input unrelated command')
            getpass('press enter to continue>>> ')
            clear_screen()
            return
    else:
        logger.info(f'{username} check the basket')
        b = Basket(username)
        b.show_basket(basket)
        getpass('Please press enter to continue>> ')

import logging
from models.basket import Basket
from shop.helpers.consts import EXIT_COMMANDS, RUNNING


logger = logging.getLogger(__name__)


def handel_compare_command(
        store_list: list,
        store: dict,
        basket: list,
        username: str
        ) -> None:
    logger.info(f'{username} wants to compare gadgets')
    items = list()
    while RUNNING:
        model = input('Enter Model or press EXIT COMMANDS>> ')
        if model in EXIT_COMMANDS:
            logger.info(f'{username} wants to exit from compare_gadgets.')
            b = Basket(username)
            gadgets = b.compare_products(store_list, store, items)
            for gadget in gadgets:
                print(f'Brand: {gadget[0]}  Model: {gadget[1]}  '
                      f'Specifications: {gadget[2]}')
                logger.info(f'{username} compared items')
            input('Press enter to continue>> ')
            break
        else:
            logger.info(f'{username} add {model} to compare list')
            items.append(model)

import logging
from models.basket import Basket
from conf import *
from getpass import getpass

logger= logging.getLogger(__name__)


def handel_search_command(store_list: list, store: dict,basket, username):
    print('You can search on MOBILE SHOP gadgets')
    logger.info(f'{username} wants to search on products')
    model= input('Model>>' ).lower()
    b= Basket(username)
    available= b.search_store(model, store_list)
    if available:
        if available[0][1] == 1.0:
            logger.info(f'{username} input exact model: {model}')
            item= available[0][1]
            print('********Available********')
            print(f'Dear , {model} is available in our MOBILE SHOP')
            print('********Available********\n\n')
        print(f'Dear These gadget are similar to your search:')
        for item in available :
            logger.info(f'{username} saw related item to {model}')
            print(f'Model: {item[0]} and Similarity Rate: {item[1]:.2f}')
        getpass('Please enter to contiue...')
    else:
        logger.warning(f'{username} input unavailable model: {model}')
        print(f'Dear ! This item is not available in out MOBILE SHOP.')
    getpass('Please enter to contiue...')
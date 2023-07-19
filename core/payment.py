from shop.handlers.email_command_handler import send_email
from shop.handlers.calculate_command_handler import (
    calculate_item,
    calculate_total_payment,
    discount_gift_card
)
from models.payment import Payment
from getpass import getpass
from models.user import UserDatabase
import logging
import random

logger = logging.getLogger(__name__)


def payment(basket: list, email: str, name: str, user):
    store = {
        'smart_phone': {
            'apple': {
                'iphone 14 pro': {
                    'price': 1_900,
                    'production_year': 2023,
                    'available': None,
                    'cpu': 'Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz)'
                    },
                'iphone 14': {
                    'price': 1_500,
                    'production_year': 2023,
                    'available': None,
                    'cpu': 'Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz)'
                    },
                'iphone 13 pro': {
                    'price': 1_000,
                    'production_year': 2021,
                    'available': None,
                    'cpu': 'Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz)'
                    },
                'iphone 13': {
                    'price': 900,
                    'production_year': 2021,
                    'available': None,
                    'cpu': 'Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz)'
                    }
            },
            'samsung': {
                'galaxy a51': {
                    'price': 600,
                    'production_year': 2020,
                    'available': None,
                    'cpu': 'Octa-core (4x2.3 GHz Cortex-A73 & 4x1.7 GHz)'
                    },
                'galaxy a10': {
                    'price': 200,
                    'production_year': 2017,
                    'available': None,
                    'cpu': 'Octa-core (2x1.6 GHz Cortex-A73 & 6x1.35 GHz)'
                    },
                'galaxy s22': {
                    'price': 1_200,
                    'production_year': 2021,
                    'available': None,
                    'cpu': 'Octa-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz)'
                    },
                'galaxy s23': {
                    'price': 1_700,
                    'production_year': 2023,
                    'available': None,
                    'cpu': 'Octa-core (1x3.36 GHz Cortex-X3 & 2x2.8 GHz)'
                    }
            }
        }
    }
    for item in basket:
        brand = item[2]
        quantity = item[1]
        model = item[0]
        price = store['smart_phone'][brand][model]['price']
        each_item_payment = calculate_item(price, quantity)
        payment = Payment(each_item_payment).bind(calculate_total_payment)
        discount = getpass(f'Dear {name}!! input gift code or press enter:')
        if user.gift_code == discount:
            payment = Payment(payment).bind(discount_gift_card)

    gift_code = random.randint(1000, 10000)
    with UserDatabase('users.json') as db:
        db.update_user_gift_code(email, gift_code)

    print(f'Dear {name}!! Your resipt fee is {payment} Euro.')
    print('we will send you an email for payment.')
    print(f'your gift code: {gift_code}')
    logger.info(f'{name} saw payment successfully.')

    to_email = email
    subject = 'Your payment fee!'
    message = f'Dear customer {name}, your order has been shipped and will arrive in 3-5 business days. Thank you for shopping with us! you should pay {payment} Euro to postman.\n Your GIFT CARD NUMBER for next buy is {gift_code}.'
    send_email(to_email, subject, message)

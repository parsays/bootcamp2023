import smtplib
from email.mime.text import MIMEText
from models.payment import Payment
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

    def calculate_item(price: int, quantity: int) -> int:
        each_item_payment = price * quantity
        return each_item_payment

    def calculate_total_payment(x: int) -> int:
        total_payment = 0 + x
        return total_payment
    for item in basket:
        brand = item[2]
        quantity = item[1]
        model = item[0]
        price = store['smart_phone'][brand][model]['price']
        each_item_payment = calculate_item(price, quantity)
        payment = Payment(each_item_payment).bind(calculate_total_payment)

    gift_code = random.randint(1000, 10000)

    with UserDatabase('users.json') as db:
        db.update_user_gift_code(email, gift_code)

    print(f'Dear {name}!! Your resipt fee is {payment} Euro.')
    print('we will send you an email for payment.')
    logger.info(f'{name} saw payment successfully.')

    def send_email(to_email, subject, message):
        # Set up the email message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'parsa.ys10@gmail.com'
        msg['To'] = to_email

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            # Log in to your email account
            smtp.login('parsa.ys10@gmail.com', 'bobkasxmbxvsjzrz')

            # Send the email message
            smtp.send_message(msg)

        print('Email sent successfully')

        logger.info('Email sent successfully')
    to_email = email
    subject = 'Your payment fee!'
    message = f'Dear customer {name}, your order has been shipped and will arrive in 3-5 business days. Thank you for shopping with us! you should pay {payment} Euro to postman.\n Your GIFT CARD NUMBER for next buy is {gift_code}.'
    send_email(to_email, subject, message)

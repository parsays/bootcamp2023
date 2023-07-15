import logging
from core.entry import clear_screen
from models.command import COMMANDS
from getpass import getpass

logger= logging.getLogger(__name__)


def jobs(username):
    basket= list()

    store= {
        'smart_phone': {
            'apple': {
                'iphone 14 pro': {'price': 1_900, 'production_year': 2023, 'available': None, 'cpu':'Hexa-core (2x3.46 GHz Everest + 4x2.02 GHz Sawtooth)'},
                'iphone 14': {'price': 1_500, 'production_year': 2023, 'available': None, 'cpu':'Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)'},
                'iphone 13 pro': {'price': 1_000, 'production_year': 2021, 'available': None, 'cpu':'Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)'},
                'iphone 13': {'price': 900, 'production_year': 2021, 'available': None, 'cpu':'Hexa-core (2x3.23 GHz Avalanche + 4x1.82 GHz Blizzard)'}
            },
            'samsung': {
                'galaxy a51': {'price': 600, 'production_year': 2020, 'available': None, 'cpu':'Octa-core (4x2.3 GHz Cortex-A73 & 4x1.7 GHz Cortex-A53)'},
                'galaxy a10': {'price': 200, 'production_year': 2017, 'available': None, 'cpu':'Octa-core (2x1.6 GHz Cortex-A73 & 6x1.35 GHz Cortex-A53)'},
                'galaxy s22': {'price': 1_200, 'production_year': 2021, 'available': None, 'cpu':'Octa-core (1x3.00 GHz Cortex-X2 & 3x2.50 GHz Cortex-)'},
                'galaxy s23': {'price': 1_700, 'production_year': 2023, 'available': None, 'cpu':'Octa-core (1x3.36 GHz Cortex-X3 & 2x2.8 GHz Cortex)'}
            }
        }
    }
    
    store_list= [('smart_phone', 'apple', 'iphone_14_pro', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'apple', 'iphone_14', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'apple', 'iphone_13_pro', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'apple', 'iphone_13', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'samsung', 'galaxy a51', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'samsung', 'galaxy a10', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'samsung', 'galaxy s22', {'price': None, 'production_year': None, 'available': None, 'cpu': None}),
                ('smart_phone', 'samsung', 'galaxy s23', {'price': None, 'production_year': None, 'available': None, 'cpu': None})]
    
    while True:
        clear_screen()
        print(f'Your Basket: {basket}')
        print('********features on this mobile shop********')
        print("1. You are able to add item by pressing ADD \n2. You are able to search in store by pressing SEARCH \n3. You are able remove item in your basket by pressing REMOVE \n4. You are able to show your basket by pressing BASKET\n5. You are able to compare gadjets by pressing COMPARE\n6. You are able to see available gadgets by pressing GADGETS.\n7. You are able to pay your bsket by pressing PAYMENT")
        print('********features on this online shop********')
        

        try:
            command = input('Please enter your command>> ')
            clear_screen()
            
            command = command.lower()
            if command in COMMANDS:
                execute_action= COMMANDS[command]
                execute_action(store_list, store, basket, username)

            if command == 'payment':
                break
        except Exception as msg:
            print(f'An error accured: {msg}')
    return basket
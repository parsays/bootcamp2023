from models.payment import Payment


def payment(basket):


    store_list= {
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

    

    def calculate_item(price, quantity): 
        each_item_payment = price * quantity
        return each_item_payment
    
    def calculate_total_payment(x):
        total_payment= 0 + x
        return total_payment
        
    for item in basket:
        brand = item[2]
        quantity = item[1]
        model = item[0]
        price = store_list['smart_phone'][brand][model]['price']
        each_item_payment=calculate_item(price, quantity)
        payment = Payment(each_item_payment).bind(calculate_total_payment)

    print(payment)
    input()

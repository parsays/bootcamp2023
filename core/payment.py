from models.payment import Payment


def payment(basket):
    store_list = [
        (
            'smart_phone',
            'apple',
            'iphone_14_pro',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'apple',
            'iphone_14',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'apple',
            'iphone_13_pro',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'apple',
            'iphone_13',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'samsung',
            'galaxy a51',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'samsung',
            'galaxy a10',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'samsung',
            'galaxy s22',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        ),
        (
            'smart_phone',
            'samsung',
            'galaxy s23',
            {
                'price': None,
                'production_year': None,
                'available': None,
                'cpu': None
            }
        )
        ]

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
        price = store_list['smart_phone'][brand][model]['price']
        each_item_payment = calculate_item(price, quantity)
        payment = Payment(each_item_payment).bind(calculate_total_payment)

    print(payment)
    input()

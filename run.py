from core.entry import entry
from core.jobs import jobs
from core.payment import payment
name = entry()
basket = jobs(name)
total = payment(basket)
print(f'THIS IS YOUR TOTAL PRICE: {total}')

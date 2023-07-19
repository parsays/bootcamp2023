from core.entry import entry
from core.jobs import jobs
from core.payment import payment
from conf import *
name = entry()
basket = jobs(name.name)
if not basket == list():
    total = payment(basket, name.email, name.name, name)
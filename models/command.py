from shop.handlers.add_command_handler import handel_add_command
from shop.handlers.search_command_handler import handel_search_command
from shop.handlers.remove_command_handler import handel_remove_command
from shop.handlers.basket_command_handler import handle_basket_command
from shop.handlers.compare_command_handler import handel_compare_command
from shop.handlers.gadgets_command_handler import handel_gadgets_command
from shop.handlers.signup_command_handler import handel_signup_command
from shop.handlers.signin_command_handler import handel_signin_command
COMMANDS = {
    'add':  handel_add_command,
    'search': handel_search_command,
    'remove': handel_remove_command,
    'basket': handle_basket_command,
    'compare': handel_compare_command,
    'gadgets': handel_gadgets_command,
}
ENTERY_COMMANDS = {
    'signup': handel_signup_command,
    'signin': handel_signin_command,
}

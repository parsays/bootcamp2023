import os
import logging
from difflib import SequenceMatcher
from shop.helpers.consts import EXIT_COMMANDS

logger = logging.getLogger(__name__)


def clear_screen():
    # Clear the screen for Windows-based systems
    if os.name == 'nt':
        os.system('cls')
    # Clear the screen for Unix/Linux/Mac-based systems
    else:
        os.system('clear')


class Basket:

    def __init__(self, username) -> None:
        self.username = username

    def add_products(
            self,
            basket: list,
            brand: str,
            model: str,
            quantity: int
            ) -> list:
        for item in basket:
            if model in item:
                logger.warning(f'{self.username} wants to add '
                               f'{model} which added before')
                print(f'Dear {self.username}! You have ADD this gadget before')
                return basket
        basket.append((model, quantity, brand))
        return basket

    def similarity(self, actual: str, keyword: str):
        return SequenceMatcher(None, actual, keyword).ratio()

    def search_store(self, model: str, store_list: list) -> list:
        similar_list = list()
        for item in store_list:
            score = self.similarity(item[2], model)
            if score >= 0.4:
                similar_list.append((item[2], score))
        similar_list = sorted(
            similar_list,
            key=lambda item: item[1],
            reverse=True
            )
        if similar_list:
            return similar_list

    def remove_products(self, basket: list, gadget: str) -> bool:
        for item in basket:
            if gadget in item:
                basket.remove((item))
                return True
        else:
            return False

    def clear_screen(self):
        # Clear the screen for Windows-based systems
        if os.name == 'nt':
            os.system('cls')
        # Clear the screen for Unix/Linux/Mac-based systems
        else:
            os.system('clear')

    def show_basket(self, basket: list) -> list:
        print("********YOUR BASKET********")
        for model, quantity in basket:
            print(f'Model: {model} and Quantity: {quantity}')
        print("********YOUR BASKET********")

    def compare_products(
            self,
            store_list: list,
            store: list,
            models: list
            ) -> list:
        print(models)
        gadgets = list()
        for item in models:
            for gadget in store_list:
                if gadget[2] == item:
                    gadgets.append((gadget[1], gadget[2], gadget[3]))
        return gadgets

    def Product_pagination(self, page_number: int) -> list:
        results = list()
        finish = page_number * 5
        results.append(finish)
        start = finish - 5
        results.append(start)
        return results

    def show_gadgets(
            self,
            finish_index: int,
            start_index: int,
            page: int,
            number_of_page: int,
            store_list: list
            ) -> None:
        while True:
            try:
                for i in range(start_index, finish_index):
                    print(f'{i+1}. Brand: {store_list[i][1]}    '
                          f'Model: {store_list[i][2]}   '
                          f'Available: {store_list[i][3]["available"]}')
                print(f'page: {page}/{number_of_page}   ')
            except IndexError:
                print(f'page: {page}/{number_of_page}')
            try:
                page = int(input('page>> '))
                clear_screen()
                if page in EXIT_COMMANDS:
                    break
                if page > number_of_page:
                    page = 1
            except ValueError:
                print(f'You have to enter number '
                      f'in range 1 to {number_of_page} ')
            if page in EXIT_COMMANDS:
                logger.info(f'{self.username} exit from adding option')
                break
            else:
                results = self.Product_pagination(page)
                start_index = results[1]
                finish_index = results[0]

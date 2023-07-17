import logging
from models.basket import Basket

logger = logging.getLogger(__name__)


def handel_gadgets_command(
        store_list: list,
        store: dict,
        basket: list,
        username: str
        ) -> None:
    logger.info(f'{username} wants to see product list')
    finish_index = 5
    start_index = 0
    page = 1
    number_of_page = len(store_list) // 5 + 1
    b = Basket(username)
    logger.info(f'{username} saw product list page: {page} ')
    b.show_gadgets(
        finish_index,
        start_index,
        page,
        number_of_page,
        store_list
        )

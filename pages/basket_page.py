from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def should_be_empty_cart_message(self):
        assert self.is_element_present(
            *BasePageLocators.EMPTY_CART_MESSAGE
        ), "Basket is not empty"

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(
            *BasePageLocators.ITEM_IN_BASKET
        ), "There are items in the cart"

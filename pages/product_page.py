from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add = self.browser.find_element(
            *ProductPageLocators.ADD_BUTTON
        )
        add.click()

    def should_be_right_message(self):
        item_name = self.browser.find_element(
            *ProductPageLocators.ITEM_NAME
        ).text
        basket_message = self.browser.find_element(
            *ProductPageLocators.BASKET_MSG
        ).text
        assert item_name == basket_message, 'Message or item is wrong!'

    def should_be_right_price(self):
        item_price = self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE
        ).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text
        assert item_price == basket_price, 'Cart price and product price are not equal!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.BASKET_MSG
        ), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.BASKET_MSG
        ), "Success message is not dissapear"

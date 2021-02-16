from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BASKET_MSG = (By.CSS_SELECTOR, ".alertinner")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>p")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")

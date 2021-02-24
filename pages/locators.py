from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    MAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASS1_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS2_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BASKET_MSG = (By.CSS_SELECTOR, ".alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main>p")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".row>h2")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


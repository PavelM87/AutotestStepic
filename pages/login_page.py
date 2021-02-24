from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.MAIL_FORM
        ).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASS1_FORM
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.PASS2_FORM
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT
        ).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login URL is invalid"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), 'Login form not found!'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM
        ), 'Registration form not found!'


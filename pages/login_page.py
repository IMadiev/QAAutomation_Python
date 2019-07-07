from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.index('login')!=-1, "URL is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FIELD), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_FIELD), "Registration password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_CONFIRM_FIELD), "Pass confirm is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT_BUTTON), "Registration button is not presented"

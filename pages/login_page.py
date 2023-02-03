import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = '123qaz789'
        self.browser.find_element(*LoginPageLocators.NAME_INPUT).send_keys(email) 
        self.browser.find_element(*LoginPageLocators.PSWD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PSWD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_SUBMIT).click()
        time.sleep(2)

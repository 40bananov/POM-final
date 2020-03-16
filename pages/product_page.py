from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла


class ProductPage(BasePage): 
    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN).click()        



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def bookname_is_valid(self):
        name_warning = self.browser.find_element(*ProductPageLocators.BOOK_ADDED).text
        assert self.is_element_present(*ProductPageLocators.BOOK_ADDED), name_warning

    def price_is_valid(self):
        price_warning = self.browser.find_element(*ProductPageLocators.BOOK_ADDED).text
        assert self.is_element_present(*ProductPageLocators.CART_SUMM), price_warning


    def guest_cant_see_success_message_after_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "есть саксес"


    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "нет саксеса"


    def test_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "не пропал"



from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN).click()        


    def bookname_is_valid(self):
        name_warning = self.browser.find_element(*ProductPageLocators.BOOK_ADDED).text
        print(f"Book is: {name_warning}")
        assert self.browser.find_element(*ProductPageLocators.BOOK_ADDED).text ==  self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, name_warning

    def price_is_valid(self):
        price_warning = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(f"Price is: {price_warning}")
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text ==  self.browser.find_element(*ProductPageLocators.CART_SUMM).text, price_warning


    def guest_cant_see_success_message_after_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "есть саксес"


    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "нет саксеса"


    def test_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "не пропал"



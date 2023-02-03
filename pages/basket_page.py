from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def look_if_cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.GOODS_IN_CART), "товары в корзине есть"
    
    def look_for_cart_is_empty_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TEXT), "текст: корзина пуста"

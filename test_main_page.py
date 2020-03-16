import pytest
#from pages.main_page import MainPage
from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    page = BasketPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_cart_page()
    page.look_if_cart_is_empty()
    page.look_for_cart_is_empty_text()



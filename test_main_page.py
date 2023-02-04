from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages import links


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    browser.get(links.LINK)
    page = MainPage(browser, links.LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.look_if_cart_is_empty()
    cart_page.look_for_cart_is_empty_text()


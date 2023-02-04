import pytest

from pages import links
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.get(links.LOGIN_LINK)
        login_page = LoginPage(browser, links.LOGIN_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        login_page.open()                      # открываем страницу
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        browser.get(links.CODERS_LINK)
        page = ProductPage(browser, links.CODERS_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.click_add_to_cart_button()          # а тут вызываем функции
        page.bookname_is_valid()
        page.price_is_valid()

    def test_user_cant_see_success_message(self, browser):
        browser.get(links.CODERS_LINK)
        page = ProductPage(browser, links.CODERS_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.guest_cant_see_success_message()    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    browser.get(links.CODERS_LINK)
    page = ProductPage(browser, links.CODERS_LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.guest_cant_see_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_should_see_login_link_on_product_page(browser):
    browser.get(links.STARS_LINK)
    page = ProductPage(browser, links.STARS_LINK)
    page.open()
    page.should_be_login_link()


#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
@pytest.mark.parametrize('link', [f"{links.CODERS_LINK}?promo=newYear",
                                  f"{links.CODERS_LINK}?promo=newYear2019"])
#@pytest.mark.parametrize('link', [f"{links.CODERS_LINK}?promo=offer0",
#                                  f"{links.CODERS_LINK}?promo=offer1",
#                                  f"{links.CODERS_LINK}?promo=offer2",
#                                  f"{links.CODERS_LINK}?promo=offer3",
#                                  f"{links.CODERS_LINK}?promo=offer4",
#                                  f"{links.CODERS_LINK}?promo=offer5",
#                                  f"{links.CODERS_LINK}?promo=offer6",
#                                  pytest.param(f"{links.CODERS_LINK}?promo=offer7", marks=pytest.mark.xfail),
#                                  f"{links.CODERS_LINK}?promo=offer8",
#                                  f"{links.CODERS_LINK}?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser, link):
#    link = f"{link}"
    browser.get(link)
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.click_add_to_cart_button()          # а тут вызываем функции
    page.solve_quiz_and_get_code()
    page.bookname_is_valid()
    page.price_is_valid()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    browser.get(links.CODERS_LINK)
    page = ProductPage(browser, links.CODERS_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.click_add_to_cart_button()          # а тут вызываем функции
    page.guest_cant_see_success_message_after_adding()    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    browser.get(links.CODERS_LINK)
    page = ProductPage(browser, links.CODERS_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.click_add_to_cart_button()          # а тут вызываем функции
    page.test_message_disappeared()    #Проверяем, что нет сообщения об успехе с помощью is_disappeared


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    browser.get(links.STARS_LINK)
    page = ProductPage(browser, links.STARS_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser.get(links.CODERS_LINK)
    page = ProductPage(browser, links.CODERS_LINK)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.look_if_cart_is_empty()
    cart_page.look_for_cart_is_empty_text()

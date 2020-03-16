from selenium.webdriver.common.by import By


class LoginPageLocators():
    NAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PSWD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PSWD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2") 
    BTN_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class BasePageLocators():
    CART_BTN = (By.CSS_SELECTOR, ".btn-group")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators():
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    GOODS_IN_CART = (By.CSS_SELECTOR, ".col-sm-6.h3")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    CART_SUMM = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div")




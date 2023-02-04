from selenium.webdriver.common.by import By


class LoginPageLocators:
    # NAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    # PSWD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    # PSWD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    # BTN_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    NAME_INPUT = (By.XPATH, "//input[@name = 'registration-email']")
    PSWD_INPUT = (By.XPATH, "//input[@name = 'registration-password1']")
    PSWD_CONFIRM = (By.XPATH, "//input[@name = 'registration-password2']")
    BTN_SUBMIT = (By.XPATH, "//button[@name = 'registration_submit']")

    @staticmethod
    def login_input_locators(block, name):
        input_locator = (By.XPATH, f"//h2[contains(text(), '{block}')]/..//label[contains(text(), '{name}')]/..//input")
        return input_locator


class BasePageLocators:
   CART_BTN = (By.CSS_SELECTOR, ".btn-group")
   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
   LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
   USER_ICON = (By.CSS_SELECTOR, ".icon-user")
#     CART_BTN = (By.XPATH, "//span[@class = 'btn-group']")
#     LOGIN_LINK = (By.XPATH, "//a[@id = 'login_link']")
#     LOGIN_LINK_INVALID = (By.XPATH, "//a[@id = 'login_link_inc']")
#     USER_ICON = (By.XPATH, "//i[@class = 'icon-user']")


class CartPageLocators:
   EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner p")
   GOODS_IN_CART = (By.CSS_SELECTOR, ".col-sm-6.h3")
#     EMPTY_CART_TEXT = (By.XPATH, "//div[@id = 'content_inner']/p")
#     GOODS_IN_CART = (By.XPATH, "//div[@class = 'basket-items']")


class ProductPageLocators:
   ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
   BOOK_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
   BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
   BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
   CART_SUMM = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
   SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div")
#     ADD_TO_CART_BTN = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
#     BOOK_ADDED = (By.XPATH, "//div[@id='messages']")
#     BOOK_NAME = (By.XPATH, "//div[contains(@class, 'alert-success')]")
#     BOOK_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
#     CART_SUMM = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
#     SUCCESS_MESSAGE = (By.XPATH, "//div[@id = 'messages']")




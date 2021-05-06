from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")


class BasketPageLocators:
    ITEMS_TABLE_HEAD = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_from")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > .btn")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p> strong")
    SUCCESS_MESSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)")
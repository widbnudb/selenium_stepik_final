import pytest
import time

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.registered_user_basket_page
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_page_link, 10)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "password1259"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, timeout=10):
        page = ProductPage(browser, link, timeout)
        page.open()
        page.should_be_success_message_absent()

    def test_user_can_add_product_to_basket(self, browser, timeout=10):
        page = ProductPage(browser, link, timeout)
        page.open()
        page.should_be_product_page()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()
        page.should_be_equal_product_name()
        page.should_be_equal_product_price()


def test_guest_cant_see_success_message(self, browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_success_message_absent()


def test_guest_can_add_product_to_basket(self, browser):
    page = ProductPage(browser, link, 10)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_product_name()
    page.should_be_equal_product_price()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_absent()



@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_about_empty_basket()
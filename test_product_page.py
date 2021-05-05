from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link, 10)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_product_name()
    page.should_be_equal_product_price()

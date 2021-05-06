from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_button()

    def should_be_product_url(self):
        assert self.is_url_correct("promo=offer"), "Incorrect url"

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button isn't presented"

    def should_be_success_message_absent(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_WITH_PRODUCT_NAME, 4), \
            "Success message is shown"

    def should_be_equal_product_name(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Product name isn't presented on " \
                                                                                   "the page"

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Product name isn't presented in " \
                                                                                   "the success message"

        expected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        actual_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert actual_product_name == expected_product_name, "Product name in the success message doesn't match the " \
                                                             "added one"

    def should_be_equal_product_price(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Product price isn't presented on " \
                                                                                   "the page"

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Product price isn't presented in " \
                                                                                   "the success message"

        expected_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        actual_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert actual_product_price == expected_product_price, "Product price in the success message doesn't match " \
                                                               "the added one"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_WITH_PRODUCT_NAME, 4), \
            "Message doesn't disappear"


from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # def should_be_basket_page(self):
    #     self.should_be_basket_url()
    #     # self.should_be_login_form()
    #     # self.should_be_register_form()

    def should_be_basket_url(self):
        assert self.is_url_correct("basket"), "Incorrect url"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TABLE_HEAD, 4), "The basket isn't empty"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "Message about empty " \
                                                                                           "basket is absent"

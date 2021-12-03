from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET).click()

    def should_be_message_about_adding_to_basket(self):
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_NAME).text

        current_name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message_name == current_name_product, f"Product {current_name_product} not added to cart"

    def should_be_message_about_price_added_to_basket(self):
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE).text

        current_price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert message_price == current_price_product, f"Product with price {current_price_product} not added to cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_WITH_NAME), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_WITH_NAME), "Success message is disappeared, but should not be"

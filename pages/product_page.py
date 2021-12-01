from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET).click()

    def should_be_message_about_adding_to_basket(self):
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_NAME).text

        #  try:
        current_name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message_name == current_name_product, f"Product {current_name_product} not added to cart"
        # except ():
        #    pass

    def should_be_message_about_price_added_to_basket(self):
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE).text
        #  try:
        current_price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert message_price == current_price_product, f"Product with price {current_price_product} not added to cart"
        # except ():
        #    pass


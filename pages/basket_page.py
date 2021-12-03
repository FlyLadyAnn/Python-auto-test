from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    # Реализуйте необходимые проверки, в том числе отрицательную
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket should be empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "Should be message 'Your basket is empty.'"

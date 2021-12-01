from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    MESSAGE_WITH_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

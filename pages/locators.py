from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BUTTON_BASKET = (By.CSS_SELECTOR, "span .btn-default[href$='/basket/']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, "#content_inner .row")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")

    EMAIL_REGISTR = (By.CSS_SELECTOR, "#id_registration-email")
    PASS1_REGISTR = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS2_REGISTR = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTR = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    MESSAGE_WITH_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

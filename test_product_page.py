from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest

#  link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/" #  товар
#  param_promo = "?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#  param_promo = "?promo=newYear2019"
param_promo = "?promo="
list_offer = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6', 'offer7', 'offer8', 'offer9']


# запуск теста с параметрами
# @pytest.mark.parametrize('offer', list_offer)
# запуск теста с параметрами, пометка упавшего "xfail"
@pytest.mark.parametrize('offer', ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',
                                   pytest.param('offer7', marks=pytest.mark.xfail),
                                   'offer8', 'offer9'])
def test_guest_can_add_product_to_basket(browser, offer):
    global link, param_promo
    link_full = link + param_promo + offer

    page = ProductPage(browser, link_full)  # Открыть страницу товара
    page.open()

    page.add_product_to_basket()  # Добавление товара в корзину
    page.solve_quiz_and_get_code()  # Считаем по формуле и вводим в поле алерта

    page.should_be_message_about_adding_to_basket()  # ОР: Сообщение о добавлении в корзину, названия должны совпадать
    page.should_be_message_about_price_added_to_basket()  # ОР: Сообщение о стоимости товара в корзине, совпадает с ценой товара на стр


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    global link

    page = ProductPage(browser, link)  # Открыть страницу товара
    page.open()

    page.add_product_to_basket()  # Добавление товара в корзину

    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    global link

    page = ProductPage(browser, link)  # Открыть страницу товара
    page.open()

    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    global link

    page = ProductPage(browser, link)  # Открыть страницу товара
    page.open()

    page.add_product_to_basket()  # Добавление товара в корзину

    page.should_be_disappeared_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_disappeared


# тесты вида "гость видит ссылку с любой страницы Х на страницу логина"
def test_guest_should_see_login_link_on_product_page(browser):
    global link
    page = ProductPage(browser, link)
    page.open()

    page.should_be_login_link()


# тесты вида "гость может перейти на страницу логина со страницы Х"
def test_guest_can_go_to_login_page_from_product_page(browser):
    global link
    page = ProductPage(browser, link)
    page.open()

    page.go_to_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    global link

    page = ProductPage(browser, link)  # Гость открывает главную страницу
    page.open()

    page.go_to_basket_page()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)

    basket_page.should_be_empty_basket()  # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket_message()  # Ожидаем, что есть текст о том что корзина пуста

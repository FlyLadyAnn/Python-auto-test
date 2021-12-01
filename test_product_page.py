from pages.product_page import ProductPage
import pytest

#  link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/" #  товар
#  param_promo = "?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#  param_promo = "?promo=newYear2019"
param_promo = "?promo="
list_offer = ['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6', 'offer7', 'offer8', 'offer9']


# @pytest.mark.parametrize('offer', list_offer)
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
    page.should_be_message_about_price_added_to_basket() # ОР: Сообщение о стоимости товара в корзине, совпадает с ценой товара на стр

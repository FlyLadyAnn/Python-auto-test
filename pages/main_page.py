from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        #  Гость открывает главную страницу
        #  Переходит в корзину по кнопке в шапке сайта
        #  Ожидаем, что в корзине нет товаров
        #  Ожидаем, что есть текст о том что корзина пуста
        pass

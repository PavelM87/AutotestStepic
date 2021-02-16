from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()                         # открываем страницу
    page.add_to_basket()                # жмем кнопку 'Добавить в корзину'
    page.solve_quiz_and_get_code()      # решаем уравнение и вводим ответ
    page.should_be_right_message()      # название товара в сообщении должно совпадать с добавленным товаром
    page.should_be_right_price()        # стоимость корзины совпадает с ценой товара

import pytest

from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

def test_guest_can_see_basket_button(browser3):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser3, link)
    page.open()
    page.button_should_exist()

@pytest.mark.skip(reason="Zadanie")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser3):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser3, link)
    page.open()
    page.no_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser3):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser3, link)
    page.open()
    page.shouldnt_see_success_message_after_opening()

@pytest.mark.skip(reason="Zadanie")
def test_message_disappeared_after_adding_product_to_basket(browser3):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser3, link)
    page.open()
    page.message_is_disappeared()

''' Комменчу так, как этот код нужен был для задания и я не хочу его менять, чтобы просто добавить skip
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser3, link):
    page = ProductPage(browser3, link)
    page.open()
    page.button_should_be_clickable()
'''

def test_guest_should_see_login_link_on_product_page(browser3):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser3, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser3):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser3, link)
    page.open()
    page.should_be_text_basket_is_empty()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser3):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser3, link)
    page.open()
    page.shouldnt_be_product_in_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser3):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser3, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser3):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser3, link)
        page.open()
        page.shouldnt_see_success_message_after_opening()

    def test_user_can_add_product_to_basket(self, browser3):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser3, link)
        page.open()
        page.button_should_be_clickable()
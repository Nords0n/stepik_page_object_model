import pytest

from .pages.base_page import BasePage
from .pages.product_page import ProductPage

# def test_guest_can_see_basket_button(browser3):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser3, link)
#     page.open()
#     page.button_should_exist()

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

def test_message_disappeared_after_adding_product_to_basket(browser3):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser3, link)
    page.open()
    page.message_is_disappeared()

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
# urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)
# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(browser3, link):
#     page = ProductPage(browser3, link)
#     page.open()
#     page.button_should_be_clickable()

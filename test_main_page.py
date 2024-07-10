import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

def test_guest_can_go_to_login_page(browser3):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser3, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser3, browser3.current_url)
    login_page.should_be_login_link()

def test_guest_should_see_login_link(browser3):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser3, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_check_login_page(browser3):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser3, link)
    page.open()
    page.should_check_login_page()
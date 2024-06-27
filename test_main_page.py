import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_go_to_login_page(browser3):
    link = "http://selenium1py.pythonanywhere.com/"
    browser3.get(link)
    login_link = browser3.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
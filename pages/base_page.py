from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser3, url, timeout=10):
        self.browser3 = browser3
        self.url = url
        self.browser3.implicitly_wait(timeout)

    def open(self):
        self.browser3.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser3.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
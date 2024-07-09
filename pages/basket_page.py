from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def should_be_text_basket_is_empty(self):
        view_basket_button = WebDriverWait(self.browser3, 10).until(
            EC.presence_of_element_located(BasketPageLocators.VIEW_BASKET_BUTTON)
        )
        view_basket_button.click()

        # empty_basket_text = WebDriverWait(self.browser3, 10).until(
        #     EC.visibility_of_element_located(BasketPageLocators.EMPTY_BASKET_TEXT)
        # ).text

        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text is not presented, something wrong"


    def shouldnt_be_product_in_basket(self):
        view_basket_button = WebDriverWait(self.browser3, 10).until(
            EC.presence_of_element_located(BasketPageLocators.VIEW_BASKET_BUTTON)
        )
        view_basket_button.click()
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text is not here and you can see some products, thats wrong"

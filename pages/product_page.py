import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException

class ProductPage(BasePage):
    def button_should_exist(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Add button doesnt exist"

    def no_success_message_after_adding_product_to_basket(self):
        self.browser3.find_element(*ProductPageLocators.BASKET_BUTTON)

        add_to_basket_button = WebDriverWait(self.browser3, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BASKET_BUTTON)
        )

        add_to_basket_button.click()

        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but shouldnt"

    def shouldnt_see_success_message_after_opening(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but shouldnt"

    def message_is_disappeared(self):
        self.browser3.find_element(*ProductPageLocators.BASKET_BUTTON)

        add_to_basket_button = WebDriverWait(self.browser3, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BASKET_BUTTON)
        )

        add_to_basket_button.click()

        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message didnt disappeared :c"
    def button_should_be_clickable(self):
        button_add = self.browser3.find_element(*ProductPageLocators.BASKET_BUTTON)

        add_to_basket_button = WebDriverWait(self.browser3, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.BASKET_BUTTON)
        )

        add_to_basket_button.click()

        time.sleep(1)

        # self.solve_quiz_and_get_code()

        # Получить название товара и цену с страницы товара
        product_name = self.browser3.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser3.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        # Ожидать появления сообщения о добавлении в корзину и получить его текст
        product_name_in_message = WebDriverWait(self.browser3, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        ).text

        # Ожидать появления сообщения о стоимости корзины и получить его текст
        basket_total = WebDriverWait(self.browser3, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_TOTAL)
        ).text

        # Проверить, что название товара в сообщении совпадает с добавленным товаром
        assert product_name == product_name_in_message, \
            f"Expected product name '{product_name}' in the message, but got '{product_name_in_message}'"

        # Проверить, что стоимость корзины совпадает с ценой товара
        assert product_price == basket_total, \
            f"Expected basket total '{product_price}', but got '{basket_total}'"
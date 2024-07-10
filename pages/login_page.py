from faker import Faker
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()

class LoginPage(BasePage):
    def should_check_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login" in self.browser3.current_url, "login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        f_email = fake.ascii_free_email()
        f_password = fake.password()

        WebDriverWait(self.browser3, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_ADDRESS_REGISTER)
        ).send_keys(f_email)

        WebDriverWait(self.browser3, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_REGITSTER)
        ).send_keys(f_password)

        WebDriverWait(self.browser3, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_CONF_REGITSTER)
        ).send_keys(f_password)

        WebDriverWait(self.browser3, 10).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTER_BUTTON)
        ).click()

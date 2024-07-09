from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_ADDRESS_LOGIN = (By.ID, "id_login-username")
    PASSWORD_LOGIN = (By.ID, "id_login-password")
    EMAIL_ADDRESS_REGISTER = (By.ID, "id_registration-email")
    PASSWORD_REGITSTER = (By.ID, "id_registration-password1")
    PASSWORD_CONF_REGITSTER = (By.ID, "id_registration-password2")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn:nth-child(3)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[text()='View basket']")
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id='content_inner']/p")


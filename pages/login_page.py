from selenium.webdriver.common.by import By
from generic.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.enter_text(self.USER_NAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

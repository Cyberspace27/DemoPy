from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    title = "Swag Labs"
    eng_partial_link_text = "English"
    wait_time_out = 5

    def __init__(self, driver):
        self.driver = driver
        # self.wait_variable = W(self.driver, self.wait_time_out)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self, *locator):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def validate_page_title(self):
        assert self.title in self.driver.title

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

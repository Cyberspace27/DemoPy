import unittest
from selenium import webdriver
from generic.conf import TestData as tData
from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("dentro del setUpClass")
        global driver
        driver = webdriver.Chrome(executable_path=tData.CHROME_EXECUTABLE_PATH)
        driver.get(tData.BASE_URL)
        global login
        login = LoginPage(driver)

    @classmethod
    def tearDown(cls):
        print("dentro del TearDownClass")
        driver.close()
        driver.quit()

    def test_login_action(self):
        print("dentro del test_login_action")
        login.do_login("standard_user", "secret_sauce")
        self.assertEqual(True, True)

    def test_swagLabs_title(self):
        print("dentro del test_swagLabs_title")
        login.validate_page_title()
        self.assertEqual(True, True)

    def test_swagLabs_title_two(self):
        print("dentro del test_swagLabs_title")


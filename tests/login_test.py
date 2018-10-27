import pytest
import time
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        global driver
        driver = self.driver
        try:
            login = LoginPage(driver)
            driver.get(utils.URL)
            login.enter_username(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            login.click_login()
            time.sleep(5)
            text = driver.title
            assert text == "abc"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            driver.save_screenshot("./screenshots/test_login_error.png")
            raise

    def test_logout(self):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

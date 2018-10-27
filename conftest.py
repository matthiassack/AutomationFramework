import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    chrome_driver_path = "/Users/matthias/PycharmProjects/AutomationFramework/drivers/geckodriver"
    firefox_driver_path = "/Users/matthias/PycharmProjects/AutomationFramework/drivers/chromedriver"
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=chrome_driver_path)
    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path=firefox_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Tests Completed")

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id("txtUsername").clear()
        self.driver.find_element_by_id("txtUsername").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtPassword").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id("btnLogin").click()

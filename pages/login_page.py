from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.username_txt = (By.NAME, "username")
        self.password_txt = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_txt).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txt).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
import os
import pytest
from pages.login_page import LoginPage
from utilities.excel_utils import get_data_from_excel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCEL_PATH = os.path.join(BASE_DIR, "testdata", "test_data.xlsx")

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("username, password, validity", get_data_from_excel(EXCEL_PATH, "LoginData"))
    def test_login_excel(self, username, password, validity):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        if validity == "valid":
            assert "dashboard" in self.driver.current_url.lower()
        else:
            assert "login" in self.driver.current_url.lower()
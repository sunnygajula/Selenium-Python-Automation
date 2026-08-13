import pytest
from pages.login_page import LoginPage
from utilities.excel_utils import get_data_from_excel
import time

excel_data = get_data_from_excel("testdata/test_data.xlsx", "Sheet1")

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("username, password, validity", excel_data)
    def test_login_ddt(self, username, password, validity):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        login_pg = LoginPage(driver)
        login_pg.enter_username(username)
        login_pg.enter_password(password)
        login_pg.click_login()
        
        time.sleep(3)
        
        if validity == "valid":
            assert "dashboard" in driver.current_url.lower()
        else:
            assert "login" in driver.current_url.lower()
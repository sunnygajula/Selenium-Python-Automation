import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import time

def test_valid_login():
    # Browser Open చేయడం
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Web Application Open చేయడం
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Page Object Model ని ఉపయోగించి Login Actions చేయడం
    login_pg = LoginPage(driver)
    login_pg.enter_username("Admin")
    login_pg.enter_password("admin123")
    login_pg.click_login()
    
    time.sleep(3)
    
    # Assertion (టెస్ట్ పాస్ అయిందో లేదో చెక్ చేయడం)
    assert "dashboard" in driver.current_url.lower()
    
    # Browser Close చేయడం
    driver.quit()
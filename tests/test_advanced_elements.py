import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_handle_alert():
    chrome_options = Options()
    # Linux & CI/CD కోసం కొత్త క్రోమ్ హెడ్‌లెస్ ఫ్లాగ్స్
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        
        alert = driver.switch_to.alert
        assert alert.text == "I am a JS Alert"
        print(f"\n[ALERT TEXT]: {alert.text}")
        alert.accept()
        
        result_text = driver.find_element(By.ID, "result").text
        assert result_text == "You successfully clicked an alert"
        
    finally:
        driver.quit()
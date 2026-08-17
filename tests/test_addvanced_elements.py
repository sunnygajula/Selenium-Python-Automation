import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_handle_alert():
    # Chrome Headless Options (Windows & Linux CI/CD రెండింటికీ సపోర్ట్ చేస్తుంది)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Selenium 4 built-in manager వాడటం (webdriver_manager అవసరం లేదు)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        # Alert ఉన్న వెబ్‌పేజీకి వెళ్లడం
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        
        # 1. Alert ని ట్రిగ్గర్ చేసే బటన్‌ని క్లిక్ చేయడం
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        
        # 2. Alert కి స్విచ్ అవ్వడం
        alert = driver.switch_to.alert
        
        # 3. Alert మెసేజ్ సరిచూసుకోవడం
        assert alert.text == "I am a JS Alert"
        print(f"\n[ALERT TEXT]: {alert.text}")
        
        # 4. Alert ఓకే (Accept) చేయడం
        alert.accept()
        
        # 5. Result ని చెక్ చేయడం
        result_text = driver.find_element(By.ID, "result").text
        assert result_text == "You successfully clicked an alert"
        
    finally:
        driver.quit()
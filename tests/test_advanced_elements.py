import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_handle_alert():
    # Headless mode కాకుండా బ్రౌజర్ ఓపెన్ అయ్యి అలర్ట్ కనిపించేలా సెటప్
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Alert ఉన్న వెబ్‌పేజీకి వెళ్లడం
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    # 1. Alert ని ట్రిగ్గర్ చేసే బటన్‌ని క్లిక్ చేయడం
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    time.sleep(1)
    
    # 2. Alert కి స్విచ్ అవ్వడం
    alert = driver.switch_to.alert
    
    # 3. Alert లోని మెసేజ్ ని సరిచూసుకోవడం
    assert alert.text == "I am a JS Alert"
    print(f"\n[ALERT TEXT]: {alert.text}")
    
    # 4. Alert ఓకే (Accept) చేయడం
    alert.accept()
    
    # 5. Result ని చెక్ చేయడం
    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You successfully clicked an alert"
    
    driver.quit()
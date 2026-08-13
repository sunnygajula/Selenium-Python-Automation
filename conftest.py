import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    # Cloud Linux సర్వర్స్ లో బ్రౌజర్ బ్యాక్‌గ్రౌండ్‌లో రన్ అవ్వడానికి Headless ఆప్షన్స్
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    request.cls.driver = driver
    
    yield driver
    
    driver.quit()
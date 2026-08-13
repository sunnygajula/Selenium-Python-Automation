import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    # Local & Headless Execution Compatibility
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    request.cls.driver = driver
    
    yield driver
    
    driver.quit()

# 📸 PyTest Hook: టెస్ట్ ఫెయిల్ అయితే ఆటోమేటిక్‌గా స్క్రీన్‌షాట్ తీసే మ్యాజిక్ లాజిక్
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = getattr(item.cls, "driver", None)
        if driver:
            # Screenshots కి ఫోల్డర్ లేకపోతే క్రియేట్ చేస్తుంది
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot saved to: {screenshot_path}")
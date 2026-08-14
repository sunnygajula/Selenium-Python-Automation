import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    request.cls.driver = driver if request.cls else None
    yield driver
    driver.quit()

# 📸 PyTest Hook: Failure వచ్చినప్పుడు ఆటోమేటిక్‌గా స్క్రీన్‌షాట్ తీసి HTML రిపోర్ట్‌కి యాడ్ చేయడానికి
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.failed and not xfail) or (report.skipped and xfail):
            # Fixture నుండి డ్రైవర్‌ను తెచ్చుకోవడం
            driver = item.funcargs.get('setup') or getattr(item.cls, 'driver', None)
            if driver:
                screenshot_dir = "reports"
                os.makedirs(screenshot_dir, exist_ok=True)
                file_name = f"{item.name}.png"
                file_path = os.path.join(screenshot_dir, file_name)
                
                driver.save_screenshot(file_path)
                if pytest_html:
                    html = f'<div><img src="{file_name}" alt="screenshot" style="width:300px;height:200px;" onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra
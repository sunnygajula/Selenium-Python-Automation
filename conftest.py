import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Class-level tests కోసం driver ని పంపుతున్నాం
    request.cls.driver = driver
    
    yield driver
    
    # Test పూర్తయ్యాక బ్రౌజర్ ఆటోమేటిక్‌గా క్లోజ్ అవుతుంది
    driver.quit()
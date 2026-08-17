from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_wikipedia_search():
    # 1. Setup Headless Chrome Options for CI/CD Runner
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        # 2. Open Wikipedia
        driver.get("https://www.wikipedia.org")
        
        # 3. Perform Search
        search_box = driver.find_element(By.ID, "searchInput")
        search_box.send_keys("Python (programming language)" + "\n")
        
        # 4. Extract Heading & Assert
        actual_heading = driver.find_element(By.ID, "firstHeading").text
        expected_heading = "Python (programming language)"
        
        assert actual_heading == expected_heading, f"Expected '{expected_heading}', but got '{actual_heading}'"
        print("SUCCESS: QA Assertion Passed!")
        
    finally:
        # 5. Always close browser even if test passes or fails
        driver.quit()
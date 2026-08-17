from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 1. CI/CD & Local Compatibility కోసం Headless Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # స్క్రీన్ లేకుండా బ్యాక్‌గ్రౌండ్‌లో రన్ అవుతుంది
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

# 2. Open Wikipedia
driver.get("https://www.wikipedia.org")

# 3. Search element
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Python (programming language)" + "\n")

# 4. Extract heading text
actual_heading = driver.find_element(By.ID, "firstHeading").text

# 5. QA Assertion
expected_heading = "Python (programming language)"
assert actual_heading == expected_heading, f"Assertion Failed: Expected '{expected_heading}', but got '{actual_heading}'"

print("SUCCESS: QA Assertion Passed! Heading matches perfectly.")

driver.quit()
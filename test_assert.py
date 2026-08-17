from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Dynamic Wait: Element దొరికే వరకు Selenium 10 సెకన్లు వెయిట్ చేస్తుంది
driver.implicitly_wait(10)

# 1. Open Wikipedia main portal (100% stable search box)
driver.get("https://www.wikipedia.org")

# 2. Find search box by ID and search
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Python (programming language)" + "\n")

# 3. Extract heading from result page
actual_heading = driver.find_element(By.ID, "firstHeading").text

# 4. QA Assertion
expected_heading = "Python (programming language)"
assert actual_heading == expected_heading, f"Assertion Failed: Expected '{expected_heading}', but got '{actual_heading}'"

print("SUCCESS: QA Assertion Passed! Heading matches perfectly.")

# 5. Close browser
driver.quit()
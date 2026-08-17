from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Open Wikipedia
driver.get("https://www.wikipedia.org")

# 2. Locate search input by ID and type "Selenium"
search_input = driver.find_element(By.ID, "searchInput")
search_input.send_keys("Selenium")

# 3. Locate search button by XPATH and click it
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

# 4. Wait 2 seconds for page to load
time.sleep(2)

# 5. Get heading text and print it
heading = driver.find_element(By.ID, "firstHeading")
print("Heading is:", heading.text)

# 6. Close browser
driver.quit()
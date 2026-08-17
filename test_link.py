from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Open Wikipedia
driver.get("https://www.wikipedia.org")

# 2. Click on 'English' using ID (More reliable than LINK_TEXT)
english_link = driver.find_element(By.ID, "js-link-box-en")
english_link.click()

# 3. Wait 2 seconds
time.sleep(2)

# 4. Print current page title
print("Current title is :", driver.title)

# 5. Close browser
driver.quit()
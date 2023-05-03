import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Open the website
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

# Type username student into username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Click on the submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(3)

# Verify that new page url contains the right url
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify that new page contains expected text
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

# Verify the logout button is displayed on the new page
logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_locator.is_displayed()

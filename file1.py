from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create an instance of the WebDriver (specify the browser driver path if needed)
driver = webdriver.Firefox()

# Open the Google homepage
driver.get("https://www.google.com")

# Find the search input element using By.ID
# search_input = driver.find_element(By.ID, "search-input")



# Verify if the search results page title contains the search query
assert "OpenAI" in driver.title

# Find the first search result link
search_result_link = driver.find_element(By.CSS_SELECTOR, ".rc .r a")

# Click on the first search result
search_result_link.click()

# Wait for the page to load
time.sleep(2)

# Verify if the page title contains "OpenAI"
assert "OpenAI" in driver.title

# Close the browser
driver.quit()

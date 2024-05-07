import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.implicitly_wait(8)

# click on the dynamic search input
country_input = driver.find_element(By.ID, "autosuggest")
country_input.click()
# Type the country name
country = "India"
print("Required country name: ", country)
country_input.send_keys(country)
# wait for 2 seconds
time.sleep(2)
# get all the dropdown list
countries = driver.find_elements(By.CSS_SELECTOR, "ul[id='ui-id-1'] li a")
# select the required country name from the dropdown
for country_name in countries:
    if country_name.text == country:
        country_name.click()
        break


# validate the selected value
print("Selected country: {}".format(country_input.get_attribute("value")))
assert country_input.get_attribute("value") == country

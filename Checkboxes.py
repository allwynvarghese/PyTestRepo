from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(8)

# collate all the checkboxes in a list
checkboxes = driver.find_elements(By.XPATH, "//input[contains(@id, 'checkBoxOption')]")

# traverse through the list to find the required checkbox
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break


# validate the selected checkbox
assert driver.find_element(By.ID, "checkBoxOption2").is_selected()



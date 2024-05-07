from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(8)

# creating the alert
driver.find_element(By.ID, "name").send_keys("Allwyn")
driver.find_element(By.ID, "alertbtn").click()

# switching to the alert popup
alert = driver.switch_to.alert
print(alert.text)
assert "Allwyn" in alert.text
alert.accept()
# alert.dismiss()



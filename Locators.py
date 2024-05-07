import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Chrome driver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
driver.implicitly_wait(8)

driver.find_element(By.NAME, "name").send_keys("Allwyn")  # username

driver.find_element(By.NAME, "email").send_keys("tster@1234.com")  # email

driver.find_element(By.ID, "exampleInputPassword1").send_keys("HelloPass")  # password

driver.find_element(By.ID, "exampleCheck1").click()  # checkbox

drop = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))  # static dropdown selection
drop.select_by_visible_text("Male")

driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()  # select radio button

driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("23.04.1988")  # enter bdate

driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()  # click on submit button

message = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

assert "Success" in message
time.sleep(5)

driver.close()










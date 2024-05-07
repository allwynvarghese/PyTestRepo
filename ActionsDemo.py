from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")  # headless mode
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

# ActionChains class to perform mouse actions
action = ActionChains(driver)

# move to element
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# right click
action.context_click(driver.find_element(By.XPATH, "test")).perform()
# click and hold
action.click_and_hold(driver.find_element(By.XPATH, "test")).perform()
# drag and drop
source = driver.find_element(By.XPATH, "")
target = driver.find_element(By.XPATH, "")
action.drag_and_drop(source, target).perform()
# double click
action.double_click(driver.find_element(By.XPATH, ""))
# scroll to element
action.scroll_to_element(driver.find_element(By.XPATH, ""))

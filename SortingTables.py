from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

products = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
newList = []

for product in products:
    print(product.text, end=", ")
    newList.append(product.text)

newList.sort()
print("\n")
for list in newList:
    print(list, end=" ")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")     # headless mode
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(4)  # implicitly wait

# search for 'ber' in the search bar
searchBar = driver.find_element(By.XPATH, "//input[@type='search']")
searchBar.click()
searchBar.send_keys("ber")

# using sleep here
time.sleep(2)

# getting all the filtered items
productNames = driver.find_elements(By.XPATH, "//div[@class='product']//h4")
expectedProducts = ["Cucumber", "Raspberry", "Strawberry"]
newProds = []

print("Selected products")
for product in productNames:
    print(product.text.split("-")[0].strip(), end= ", ")
    newProds.append(product.text.split("-")[0].strip())
    # adding the items to cart using chaining selectors
    product.find_element(By.XPATH, "./following-sibling::div/button").click()

# compare two lists
assert expectedProducts.__eq__(newProds)

# go to the cart
driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()

# proceed to cart button in cart preview
driver.find_element(By.CSS_SELECTOR, "div.cart-preview div button").click()

# enter promo code
promoCode = driver.find_element(By.CSS_SELECTOR, "input.promoCode")
promoCode.click()
promoCode.send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()

# using WebDriverWait to check if the promo code is applied
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@style, 'green') and contains(text(), 'Code applied')]")))

# assert discount
discountPercent = driver.find_element(By.CSS_SELECTOR, "span.discountPerc").text
print("\nApplied discount {}".format(discountPercent))

try:
    assert "10" in discountPercent
except Exception as e:
    print(e)


# functional test 1 - check the total of the products
sum = 0
totalList = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(5) p")

for price in totalList:
    sum += int(price.text)

print("Calculated total is {}".format(sum))

totalPrice = driver.find_element(By.CSS_SELECTOR, "span.totAmt").text

# assert if calculated price == totalPrice
try:
    assert sum == totalPrice
except Exception as e:
    print(e)

# check if discounted price is < total price after applying coupon
discountedPrice = totalPrice
if float(discountPercent.strip("%")) > 0:
    discountedPrice = float(driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text)
    print("Discounted total", discountedPrice)
    assert float(totalPrice) > discountedPrice

driver.quit()









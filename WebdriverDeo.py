from selenium import webdriver  # import selenium library

# using service class in case the web browser and webdriver is not compatible

# service_obj = Service("path of webdriver")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()  # create a object for chrome webdriver

driver.get("https://rahulshettyacademy.com")  # open browser

driver.maximize_window()

print(driver.title)  # get title
print(driver.current_url)


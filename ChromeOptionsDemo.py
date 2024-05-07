from selenium import webdriver

chromeOption = webdriver.ChromeOptions()
chromeOption.add_argument("headless")  # use headless mode
chromeOption.add_argument("--start-maximized")
chromeOption.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chromeOption)

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#
# service_obj = Service()

# service_obj= Service("/Users/rohanpal/Downloads/chromedriver-mac-arm64")
# driver= webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com")


driver= webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)







time.sleep(10)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("Rohan")
# driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("1234567890")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("1234567890")
# driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("1234567890")(this one will also work)
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("1234567890")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(500)
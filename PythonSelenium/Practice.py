import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")


#ID,Xpath,CSS_Selector,Class_Name, Name, LinkText
driver.find_element(By.NAME, "email").send_keys("helloRohan@gmail.com")
driver.find_element(By.NAME, "name").send_keys("Rohan")
# female_radio_button = driver.find_element(By.CSS_SELECTOR, "div.col-sm-3:nth-of-type(2) input[type='radio']")
# female_radio_button.click()
driver.find_element(By.XPATH, "//label[text()='Female']/preceding-sibling::input[@type='radio']").click()

driver.find_element(By.ID, "mobile").send_keys("1234567890")
driver.find_element(By.XPATH,"(//input[@type='date'])").send_keys("24032000")

driver.find_element(By.NAME, "subjects").send_keys("Programming")
driver.find_element(By.XPATH, "//label[text()='Sports']/preceding-sibling::input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//label[text()='Music']/preceding-sibling::input[@type='checkbox']").click()
driver.find_element(By.ID, 'picture').send_keys("/Users/rohanpal/PycharmProjects/PythonTesting/pythonProject3/PythonSelenium/Upload.jpeg")
# driver.find_element(By.XPATH,"(//input[@type='picture'])[1]").send_keys("Hello")
driver.find_element(By.CSS_SELECTOR, 'textarea.form-control').send_keys("Beldanga,Peardoba,722145,West Bengal")
# Select(driver.find_element(By.ID, 'state')).select_by_value("NCR")
driver.find_element(By.XPATH, "//option[text()='Uttar Pradesh']").click()
Select(driver.find_element(By.NAME, 'city')).select_by_value("Agra")

# driver.find_element(By.XPATH, "//input[@type='Login']").click()

time.sleep(500)
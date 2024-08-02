import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")


#ID,Xpath,CSS_Selector,Class_Name, Name, LinkText
driver.find_element(By.NAME, "email").send_keys("helloRohan@gmail.com")
#driver.find_element(By.NAME, "name").send_keys("Rohan")
driver.find_element(By.ID , "exampleInputPassword1").send_keys("Rohan@1234")
driver.find_element(By.ID, "exampleCheck1").click()
#driver.find_element(By.ID, "exampleFormControlSelect1").selectByVisibleText()
#(driver.find_element(By.XPATH, "(//input[@id='exampleFormControlSelect1'])")
#driver.find_element(By.CSS_SELECTOR, "input[id='exampleFormControlSelect1']").send_keys("Female")

#Select(driver.find_element(By.ID,'exampleFormControlSelect1')).select_by_visible_text('Female')
Select(driver.find_element(By.ID,'exampleFormControlSelect1')).select_by_index(1)
#Select(driver.find_element(By.ID,'exampleFormControlSelect1')).select_by_value("Value name") #[if the value is present in the code]



#Xpath //tagname[@attribute='value'] -> //# input[@type='Submit']
#CSS //tagname[@attribute='value'] -> //input[@type='Submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rohan Pal")
#driver.find_element(By.XPATH,"(//input[@name='name'])[1]").send_keys("Rohan")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message= driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message
driver.find_element(By.XPATH,"(//input[@type='date'])[1]").send_keys("24032000")

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(500)
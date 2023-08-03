#driver that need
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#open site of digikala
driver.get("https://www.digikala.com") 


#time for wait execut befor code
time.sleep(5)


# click on login bottom
driver.find_element(By.XPATH, '//a[@class="styles_Link__RMyqc"]').click()

# data of mail , password
mail ="r.hosseinmardi2019@gmail.com"
password = "Mardi@1402"
time.sleep(5)


# send the mail  to the input field
driver.find_element(by=By.NAME, value='username').send_keys(mail) # enter username
driver.find_element(by=By.TAG_NAME, value='form').submit()
time.sleep(2)

# send the password  to the input field
driver.find_element(by=By.NAME, value='password').send_keys(password) # enter password
driver.find_element(by=By.TAG_NAME, value='form').submit()
time.sleep(5)

# open profile
driver.find_element(By.XPATH, '//div[@class="d-flex"]').click()
time.sleep(5)

#test name is correct or not
txtusername = driver.find_element(By.XPATH, '//span[@class="text-subtitle-strong"]').text
if(txtusername=="راضیه حسین مردی"):
    print("[!] Login failed")
   
else:
    
    print("[+] Login successful") 
   


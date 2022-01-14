from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from py_console import console
import time

#_ path for the webdriver
PATH = "/home/jonny/Documents/Projects/funs/chromedriver"

#_ options before starting the task
chromium_options = Options()
chromium_options.add_argument("--user-data-dir=/home/jonny/Documents/Projects/funs/app/userdata") ## This will be an empty folder initially 
## and cookie will be sotred here for later use
# chromium_options.add_argument("--headless")

#_ start the webdriver
driver = webdriver.Chrome(PATH,options=chromium_options)
driver.get("https://sis.erp.bits-pilani.ac.in/psc/sisprd/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL") ## opens up the particular page

#_ find sutdent system and click on it
# table = driver.find_elements_by_tag_name("tr")
# console.success("[SUCCESS] : student system row found")

# studentSystemButton = table[2].find_element_by_class_name("btn")
# studentSystemButton.click()

#! Home ERP Page Reached
## wait for it to load completely and click on registration page button
try:
    console.log("trying")
    driver.implicitly_wait(10)
    registrationPageBtn = driver.find_element_by_id("win0divPTNUI_LAND_REC_GROUPLET$2")
    print(registrationPageBtn)
    registrationPageBtn.click()
    # registrationPageBtn = WebDriverWait(driver,30).until(
    #     EC.presence_of_element_located((By.ID,"win0divPTNUI_LAND_REC_GROUPLET$2"))
    # )
    # console.success("[SUCCESS] : Logged In to ERP. Home Page Reached")
    # registrationPageBtn.click()
    
    
except Exception as e: # work on python 3.x
    console.error(str(e))
    

## now we have to wait until the clicked page loads 
## hence we use a try and except statement
# try:
#     beginnerpytut = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
#     )
#     beginnerpytut.click()

#     getstarted = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.ID,"sow-button-19310003"))
#     )
#     getstarted.click()
#     driver.back()
#     driver.back()
#     driver.back()
#     driver.forward()
#     driver.forward()
#     print("DONE NAVIGATING")
# except:
#     driver.quit()
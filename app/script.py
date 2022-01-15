from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from py_console import console
import time

#_ path for the webdriver
PATH = "/home/anish/environments/selen/chromedriver"

#_ options before starting the task
chromium_options = Options()
chromium_options.add_argument("--user-data-dir=/home/anish/enivronments/selen/app/userdata") #* This will be an empty folder initially 
#* and cookie will be sotred here for later use
# chromium_options.add_argument("--headless")

#_ start the webdriver
driver = webdriver.Chrome(PATH,options=chromium_options)
driver.get("https://erp.bits-pilani.ac.in/") #* opens up the particular page

#_ find sutdent system and click on it
table = driver.find_elements_by_tag_name("tr")
console.success("[SUCCESS] : Student System row found")

studentSystemButton = table[2].find_element_by_class_name("btn")
studentSystemButton.click()

## Home ERP Page Reached
#* wait for it to load completely and click on registration page button
#! Opens in a new tab
try:
    #_ Switch tabs
    windowHandles = driver.window_handles
    driver.switch_to.window(windowHandles[1])
    console.success("[SUCCESS] : Logged In to ERP. Home Page Reached")

    registrationPageBtn = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"win0divPTNUI_LAND_REC_GROUPLET$2"))
    )    
    registrationPageBtn.click()  
    console.success("[SUCCESS] : Registration Page Reached")
except:
    #TODO FINISH THIS LATER
    console.warn("[WARNING] : Couldn't fetch link. Using Hardcoded link . . .")
    #driver.get("https://sis.erp.bits-pilani.ac.in/psc/sisprd_newwin/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=ADMN_REGISTRATION&PTPPB_GROUPLET_ID=STUDENT_REGISTRATION&CRefName=ADMN_NAVCOLL_3")
try:
    #_ Hit Add Classes on the sidebar
    console.log("[LOG] : Trying to fetch button from sidebar")
    addClassesBtn = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"win4divPTGP_STEP_DVW_PTGP_STEP_BTN_GB$2"))
    )
    addClassesBtn.click()
    console.log("[SUCCESS] : Add Classes Page Reached")
except:
    console.warn("[WARNING] : Clicking Add classes on sidebar failed")
try:
    #_ Hit search classes at the top bar
    searchBtn = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#PSTAB > table > tbody > tr > td:nth-child(1) > a"))
    )
    searchBtn.click()
    console.log("[SUCCESS] : Search for course page reached")
except:
    console.warn("[WARNING] : Clicking search in top bar failed")


    

#* now we have to wait until the clicked page loads 
#* hence we use a try and except statement
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
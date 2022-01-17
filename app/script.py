from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
chromium_options.add_argument("--headless")

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
#_ Hit Add Classes on the sidebar
try:
    console.log("[LOG] : Trying to fetch button from sidebar")
    printPage = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"DERIVED_SSR_FL_PRINT_BUTTON"))
    )
    addClassesBtn = driver.find_element_by_id("win7divPTGP_STEP_DVW_PTGP_STEP_BTN_GB$2")
    addClassesBtn.click()
    console.success("[SUCCESS] : Add Classes Page Reached")
except:
    console.warn("[WARNING] : Clicking Add classes on sidebar failed")
    console.warn("[WARNING] : Using Hardcoded link . . .")
    driver.get("https://sis.erp.bits-pilani.ac.in/psc/sisprd_newwin/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?NavColl=true")
    console.success("[SUCCESS] : Add Classes Page Reached through Hard Link")
#_ Hit search classes at the top bar
try:
    searchBtn = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#PSTAB > table > tbody > tr > td:nth-child(1) > a"))
    )
    searchBtn.click()
    console.success("[SUCCESS] : Search for course page reached")
except:
    console.warn("[WARNING] : Clicking search in top bar failed")

#_ Uncheck the "show only open classes checkbox"
try:
    checkBox = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"SSR_CLSRCH_WRK_SSR_OPEN_ONLY$3"))
    )
    checkBox.click()
    console.success("[SUCCESS] : Show only open classes unchecked")
except:
    console.warn("[WARNING] : Showing only open classes is still checked")

#_ Fill in the search field
try:
    subjSearch = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"SSR_CLSRCH_WRK_SUBJECT_SRCH$0"))
    )
    subjSearch = Select(driver.find_element_by_id("SSR_CLSRCH_WRK_SUBJECT_SRCH$0"))
    console.info("[INFO] : Filling in Subject . . .")
    subjSearch.select_by_visible_text("BITS")
    subjCodeInput = driver.find_element_by_id("SSR_CLSRCH_WRK_CATALOG_NBR$1")
    console.info("[INFO] : Filling in Course code . . .")
    subjCodeInput.send_keys("F464")
    subjCodeInput.send_keys(Keys.RETURN)
    console.success("[SUCCESS] : Search Success")
    console.info("[INFO] : Navigating to course details")
except:
    console.warn("[WARNING] : Failed to get search subject field")
#_ Navigate to course details
try:
    subjDeets = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"MTG_CLASSNAME$0"))
    )
    subjDeets.click()
    console.success("[SUCCESS] : Reached Subject Details Page")
except:
    console.warn("[WARNING] : Couldn't find details link ")
#_ Fetch available seats count
try:
    availSeats = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.ID,"SSR_CLS_DTL_WRK_AVAILABLE_SEATS"))
    )
    console.success("[SUCCESS] : Fetched number of available seats")
    console.success(availSeats.text,severe=True)
    noOfavailSeats = int(availSeats.text)
    while noOfavailSeats > 0:
        console.error("[NOOB GET HERE]")
        time.sleep(2)
        driver.refresh()
except:
    console.warn("[WARNING] : Couldn't fetch available seats row")
    

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
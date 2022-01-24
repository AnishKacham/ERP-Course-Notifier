from unicodedata import name
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from py_console import console
from playsound import playsound
import time
import threading
import os
        

#_ path for the webdriver
PATH = "/home/anish/environments/selen/chromedriver"

#_ options before starting the task
chromium_options = Options()
chromium_options.add_argument("--user-data-dir=/home/anish/environments/selen/app/userdata") #* This will be an empty folder initially 
#* and cookie will be sotred here for later use
# chromium_options.add_argument("--headless")

#_ User inputs
song = '/home/anish/environments/selen/app/beep-07a.wav'
courses = ["HSS F346","HSS F363"]
threads =[]

#_ Thread And Related Functions
def threadSpawner(courses):
    for course in courses :
        console.info(f"[INFO] : Creating thread for {course}")
        t = threading.Thread(name=course,target=courseSearch,args=(course,))
        threads.append(t)
        t.start()
        t.join()
        driver.refresh()

def courseSearch(course):
    courseCode = course.split()
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
        subjSearch.select_by_visible_text(courseCode[0])
        subjCodeInput = driver.find_element_by_id("SSR_CLSRCH_WRK_CATALOG_NBR$1")
        console.info("[INFO] : Filling in Course code . . .")
        subjCodeInput.send_keys(courseCode[1])
        subjCodeInput.send_keys(Keys.RETURN)
        console.success("[SUCCESS] : Search Success")
        console.info("[INFO] : Navigating to course details")

    except:
        console.warn("[WARNING] : Failed to fetch course search field")
    
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
        noOfavailSeats = int(availSeats.text)
        console.success(noOfavailSeats,severe=True)
        if noOfavailSeats > 0:
            for i in range(4):
                playsound(song)
                time.sleep(0.5)
            console.success(f"[ALERT] : {course} is open",severe=True)

    except:
        console.warn("[WARNING] : Couldn't fetch available seats row")


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
    addClassesBtn = WebDriverWait(driver,30).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/form/div[2]/div[4]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[3]/div[2]/div"))
    )
    # addClassesBtn = driver.find_element_by_xpath("/html/body/form/div[2]/div[4]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[3]/div[2]/div")
    addClassesBtn.click()
    console.success("[SUCCESS] : Add Classes Page Reached")
except:
    console.warn("[WARNING] : Clicking Add classes on sidebar failed")
    console.warn("[WARNING] : Using Hardcoded link . . .")
    driver.get("https://sis.erp.bits-pilani.ac.in/psc/sisprd_newwin/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?NavColl=true")
    console.success("[SUCCESS] : Add Classes Page Reached through Hard Link")
#_ Hit search classes at the top bar
try:
    searchBtn = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#PSTAB > table > tbody > tr > td:nth-child(1) > a"))
    )
    searchBtn.click()
    console.success("[SUCCESS] : Search for course page reached")
except:
    console.warn("[WARNING] : Clicking search in top bar failed")
    console.info("[INFO] : Using Hard Coded Link . . .")
    driver.get("https://sis.erp.bits-pilani.ac.in/psc/sisprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL?Page=SSR_CLSRCH_ENTRY&Action=U&ACAD_CAREER=CAR&EMPLID=41120190091&ENRL_REQUEST_ID=&INSTITUTION=INST&STRM=TERM")

#_ Get the seats in the courses
while(1):
    threadSpawner(courses)

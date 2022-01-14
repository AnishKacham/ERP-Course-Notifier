from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#_ path for the webdriver
PATH = "/home/anish/environments/selen/chromedriver"

#_ options before starting the task
chromium_options = Options()
# chromium_options.add_argument("--headless")

#_ start the webdriver
driver = webdriver.Chrome(PATH,options=chromium_options)
driver.get("https://techwithtim.net") ## opens up the particular page

link = driver.find_element_by_link_text("Python Programming")
link.click()

## now we have to wait until the clicked page loads 
## hence we use a try and except statement
try:
    beginnerpytut = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    beginnerpytut.click()

    getstarted = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"sow-button-19310003"))
    )
    getstarted.click()
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
    print("DONE NAVIGATING")
except:
    driver.quit()
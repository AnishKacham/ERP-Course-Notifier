from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chromium_options = Options()
# chromium_options.add_argument("--headless")

PATH = "/home/anish/environments/selen/chromedriver"
driver = webdriver.Chrome(PATH,options=chromium_options); 
driver.get("https://www.techwithtim.net") 
# driver.get("https://www.notion.so")
print(driver.title)
search = driver.find_element_by_name("s")
# search = driver.find_element_by_class_name("jsx-132967223")
search.send_keys("test")
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"main"))
    )
    articles = driver.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
        print("------------------------------------------------")
finally:
    driver.quit()
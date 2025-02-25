from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options

import getForumInfo
import getForums
import getUserData 
import linkGrabber
import getCategoriesData
import getMessagesData
import dbUtils

# dbUtils.createCategoriesDB()
# dbUtils.insertCategories(getCategoriesData.getCategoriesDataByUrl('https://otomotiv-forum.com/'))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                         options=Options().add_argument("--disable-blink-features=AutomationControlled"))
driver.get('https://otomotiv-forum.com/categories/104/')
WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-template="category_view"]'))
    )

dbUtils.createTopicsDB()
print(dbUtils.forumsId())
for i in range(208):
    dbUtils.insertTopics(getForumInfo.getForumsDataById(i, driver))



#dbUtils.createUserDb()
#dbUtils.createMessagesDB()
#dbUtils.createCategoriesDB()
#dbUtils.createTopicsDB()
# categories_data = getCategoriesData.getCategoriesDataByUrl("https://otomotiv-forum.com/")
# print(categories_data)
#dbUtils.insertCategories(categories_data)

#getMessagesData.getAllMessage('https://otomotiv-forum.com/threads/volvo-xc60-2-4-dizel-2012g-akpp-pcm.43823/')
#getCategoriesData.getCategoriesDataByUrl('https://otomotiv-forum.com/')
#getForums.getForumsDataById(29)
#getForumInfo.getForumsDataById(116)

#getMessagesData.getAllMessage('https://otomotiv-forum.com/threads/pomosch-s-registraciej-na-mhh-auto.30392/')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=Options().add_argument("--disable-blink-features=AutomationControlled"))
# test = getUserData.getUserDataByUrl('https://otomotiv-forum.com/members/jurec.2862/#about', driver)
# print(test)
#dbUtils.insertUser(test)
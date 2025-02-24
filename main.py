from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import getUserData 
import linkGrabber
import getCategoriesData
import getMessagesData
import dbUtils


#dbUtils.createUserDb()
#dbUtils.createMessagesDB()
# dbUtils.createCategoriesDB()
# categories_data = getCategoriesData.getCategoriesDataByUrl("https://otomotiv-forum.com/")
# print(categories_data)
#dbUtils.insertCategories(categories_data)

getMessagesData.getAllMessage('https://otomotiv-forum.com/threads/volvo-xc60-2-4-dizel-2012g-akpp-pcm.43823/')

#getMessagesData.getAllMessage('https://otomotiv-forum.com/threads/pomosch-s-registraciej-na-mhh-auto.30392/')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=Options().add_argument("--disable-blink-features=AutomationControlled"))
# test = getUserData.getUserDataByUrl('https://otomotiv-forum.com/members/jurec.2862/#about', driver)
# print(test)
#dbUtils.insertUser(test)
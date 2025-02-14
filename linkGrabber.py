import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import getUserData

categories = ["https://otomotiv-forum.com/categories/otomotiv-forum-com.1/",
                      "https://otomotiv-forum.com/categories/chip-tjuning.8/",
                      "https://otomotiv-forum.com/categories/remont-i-diagnostika-avtomobilej.19/",
                      "https://otomotiv-forum.com/categories/moto-kommercheskij-i-vodnyj-transport.104/",
                      "https://otomotiv-forum.com/categories/avtoehlektronika.29/",
                      "https://otomotiv-forum.com/categories/oborudovanie-dlja-raboty.35/",
                      "https://otomotiv-forum.com/categories/kommercheskij-razdel.39/",
                      "https://otomotiv-forum.com/categories/svobodnyj-forum.50/"]
# выше расположены все категории сайта (мне было лень их из кода вытаскивать)

def getLinksForThreadsData():
    for URL in categories:
        page = requests.get(URL)
        src = page.text
        soup = BeautifulSoup(src, 'lxml')
        for category in soup.find_all('a'): # выгрузка форумов страницы
            if str(category.get('href'))[0:7] == "/forums":
                page = requests.get("https://otomotiv-forum.com/"+category.get('href'))
                src = page.text
                soup = BeautifulSoup(src, 'lxml')
                for forum in soup.find_all('a'): # выгрузка тем страницы
                    if str(forum.get('href'))[0:8] == "/threads":
                        page = requests.get("https://otomotiv-forum.com/"+category.get('href'))
                        src = page.text
                        soup = BeautifulSoup(src, 'lxml')
                        for thread in soup.find_all('a'):# здесь будет выгрузка сообщений на странице\
                            print("https://otomotiv-forum.com"+thread.get('href')) # здесь должно выкидывать текст сообщения, но я пока не понял как


def getUserDataViaThreads():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # подключаем драйвер
    last_link = ""
    page = requests.get("https://otomotiv-forum.com/members/list/")
    src = page.text
    soup = BeautifulSoup(src, 'lxml')
    for category in soup.find_all('a'): # выгрузка ссылок на форумы страницы
        if str(category.get('href'))[0:7] == "/forums":
            page = requests.get("https://otomotiv-forum.com/"+category.get('href'))
            src = page.text
            soup = BeautifulSoup(src, 'lxml')
            for forum in soup.find_all('a'): # выгрузка ссылок на темы страницы
                if str(forum.get('href'))[0:8] == "/threads":
                    page = requests.get("https://otomotiv-forum.com/"+category.get('href'))
                    src = page.text
                    soup = BeautifulSoup(src, 'lxml')
                    for thread in soup.find_all('a'):# здесь выгрузка ссылок на пользователей
                        if str(thread.get('href'))[0:8] == "/members" and len(str(thread.get('href'))) > 14 and str(thread.get('href')) != last_link:
                            last_link = str(thread.get('href')) # установка предыдущего профиля. Необходимо для меньшего повторения данных
                            try: # проверка на доступность профиля.
                                print(getUserData.getUserDataByUrl("https://otomotiv-forum.com"+thread.get('href'), driver))
                            except:
                                print("нет доступа к профилю: https://otomotiv-forum.com"+thread.get('href'))
    close.driver()
    
def getUserDataViaThreads():
##    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # подключаем драйвер
    previous_users = []
    users = []
    newly_registered = []
    
    
    page = requests.get("https://otomotiv-forum.com/members/list/")
    src = page.text
    soup = BeautifulSoup(src, 'lxml')
    # выгрузка новых пользователей
    for second_page in soup.find_all('a'):
        for i in range(len(users)):
            if users[i] == previous_users[i]:
                newly_registered.append(users[i])
    #"/members/list/?page=2"
    for
        if str(thread.get('href'))[0:8] == "/members" and len(str(thread.get('href'))) > 14 and str(thread.get('href')) != last_link:
            users.append(str(thread.get('href')))
        
            
##            try: # проверка на доступность профиля.
##                print(getUserData.getUserDataByUrl("https://otomotiv-forum.com"+thread.get('href'), driver))
##            except:
##                print("нет доступа к профилю: https://otomotiv-forum.com"+thread.get('href'))
##    
##    close.driver()   
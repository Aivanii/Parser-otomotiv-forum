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
                        page = requests.get("https://otomotiv-forum.com/"+forum.get('href'))
                        src = page.text
                        soup = BeautifulSoup(src, 'lxml')
                        for thread in soup.find_all('a'):# здесь будет выгрузка сообщений на странице\
                            print("https://otomotiv-forum.com"+thread.get('href')) # здесь должно выкидывать текст сообщения, но я пока не понял как
    
def getUserDataViaThreads():
    users = [] # временный массив, для сохранения инфы юзверов. Заменить на БД
    # массив необходимый для отсечения ссылок повторяющихся каждую страницу
    not_to_check =[]
    # выгрузка юзеров с первой страницы, включая недавно зарегистрировавшихся
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # подключаем драйвер
    page = requests.get("https://otomotiv-forum.com/members/list/", {"page": "1"})
    src = page.text
    soup = BeautifulSoup(src, 'lxml')

    last_link = ""
    for first_page in soup.find_all('a'):
        if str(first_page.get('href'))[0:8] == "/members" and len(str(first_page.get('href'))) > 14 and str(first_page.get('href'))[9:11] != "li" and str(first_page.get('href'))[9:11] != "?k" and str(first_page.get('href')) != last_link:
            not_to_check.append(str(first_page.get('href')))
            try: # проверка на доступность профиля.
                users.append(getUserData.getUserDataByUrl("https://otomotiv-forum.com"+first_page.get('href'), driver))
            except:
                print("нет доступа к профилю: https://otomotiv-forum.com"+first_page.get('href'))
        last_link = str(first_page.get('href'))
    
    # выгрузка оставшихся юзеров
    i = 2
    while True:
        page = requests.get("https://otomotiv-forum.com/members/list/", {"page": str(i)})
        print("страница №"+str(i)) # дебаг инфа
        src = page.text
        soup = BeautifulSoup(src, 'lxml')
        for UsersList in soup.find_all('a'):
            if str(UsersList.get('href'))[0:8] == "/members" and len(str(UsersList.get('href'))) > 14 and str(UsersList.get('href'))[9:11] != "li" and str(UsersList.get('href'))[9:11] != "?k" and str(UsersList.get('href')) != last_link:
                check = True
                for j in range(len(not_to_check)): # проверка на нового пользователя
                    if str(UsersList.get('href')) == not_to_check[j]:
                        check = False
                if check == True:
                    try: # проверка на доступность профиля.
                        users.append(getUserData.getUserDataByUrl("https://otomotiv-forum.com"+UsersList.get('href'), driver))
                    except:
                        print("нет доступа к профилю: https://otomotiv-forum.com"+UsersList.get('href'))
            last_link = str(UsersList.get('href'))
        i += 1

    driver.close() # закрытие драйвера
getUserDataViaThreads()

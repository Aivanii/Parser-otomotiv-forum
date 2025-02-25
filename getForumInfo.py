import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options


def getForumsDataById(forum_id):
   # url = f"https://otomotiv-forum.com/forums/{id}/page-{page_num}"

    # Массив для категорий
    themes =[]
    # Navigating to the page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=Options().add_argument("--disable-blink-features=AutomationControlled"))
    url = f"https://otomotiv-forum.com/forums/{forum_id}"
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-template="forum_view"]'))
    )
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # получаем количество страниц с темами на форуме
    page_count = int(soup.find_all(class_='pageNav-page')[-1].find('a').text)
    print(page_count)



    for page_num in range(1, page_count+1):
        url = f"https://otomotiv-forum.com/forums/{forum_id}/page-{page_num}"
        driver.get(url)
        print(url)
        # Анализируем страницу с помощью BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        themes_info_class_names = re.findall(r'js-inlineModContainer js-threadListItem-\d+',
                                 str(soup.find(class_='structItemContainer')))


        for theme_info_class_name in themes_info_class_names:
            theme = {}
            theme_info = soup.find(class_=lambda x: x and theme_info_class_name in x)
            # пример функции  print(soup.find(class_=(lambda x:x and theme_info_class_name in x))['data-author'] )
            # сохраняем название темы
            name = theme_info.find(class_='structItem-title').text

            # получаем id темы
            theme_id = re.findall(r'\d+', theme_info_class_name)[0]

            # получаем id пользователя создавшего форум
            creator_id = theme_info.find(class_='structItem-iconContainer').find('a')['data-user-id']

            # получем дату создания темы
            create_date = theme_info.find(class_='structItem-startDate').find(class_='u-dt')['title']

            # сохраняем число просмотров
            views = theme_info.find(class_='pairs pairs--justified structItem-minor').find('dd').text

            # сохраняем количество овтетов
            answers = theme_info.find(class_='pairs pairs--justified').find('dd').text

            # записываем полученные данные
            theme["name"] = name
            theme["theme_id"] = theme_id
            theme["parent_forum_id"] = str(forum_id)
            theme["creator_id"] = creator_id
            theme["create_date"] = create_date
            theme['views']= views
            theme['answers'] = answers
            #добовляем в общий список тем
            themes.append(theme)





    print(themes)
"""{
       name,
       theme_id,
       parent_forum_id,
       creator_id,
       create_date,
       views,
       answers
  }"""

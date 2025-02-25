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


def getForumsDataById(id,driver):
    url = f"https://otomotiv-forum.com/categories/{id}/"
    # Массив для категорий
    forums =[]
    # Navigating to the page

    driver.get(url)
    print(url)
    # Ждем, когда нужный нам элемент загрузится


    # Получаем исходный код страницы
    page_source = driver.page_source
    # Анализируем страницу с помощью BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    forums_info_id = re.findall(r'node node--id\d+ node--depth2 node--forum node--unread',
                                       str(soup.find(class_='p-body-content')))
   # print(forums_info_id)
    for forum_info_id in forums_info_id:
        forum= {}
        # получаем инфу о форуме
        forum_info = soup.find(class_=forum_info_id)

        # сохраняем название форума
        name = forum_info.find(class_='node-title').find('a').text

        # сохраняем id форума
        forum_id = re.findall(r'\d+', forum_info_id)[0]

        # сохраняем инфу о количестве тем в форуме
        themes_count =  forum_info.find(class_='pairs pairs--rows').find('dd').text

        # сохраняем кол-во сообщений  на форуме
        message_count = forum_info.find_all(class_='pairs pairs--inline')[1].find('dd').text


        # сохраняем данные
        forum['forum_id'] = forum_id
        forum['name'] = name
        forum['themes_count'] = themes_count
        forum['message_count'] = message_count

        forums.append(forum)

    return forums


"""{
       name,
       forum_id,
       themes_count,
       messages_count
  }"""

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


def getForumsDataById(id):
    url = f"https://otomotiv-forum.com/forums/{id}/"
    # Массив для категорий
    themes =[]
    # Navigating to the page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=Options().add_argument("--disable-blink-features=AutomationControlled"))
    driver.get(url)
    print(url)
    # Ждем, когда нужный нам элемент загрузится
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-template="category_view"]'))
    )

    # Получаем исходный код страницы
    page_source = driver.page_source
    # Анализируем страницу с помощью BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    





"""{
       name,
       theme_id,
       parent_forum_id,
       creator_id,
       date,
       views,
       answers
  }"""

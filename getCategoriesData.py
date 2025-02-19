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


def getCategoriesDataByUrl(url):
    # массив для категорий
    categories = []
    # Navigating to the page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=Options().add_argument("--disable-blink-features=AutomationControlled"))
    driver.get(url)

    # Ждем когда нужный нам элемент загрузится
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-template="forum_list"]'))
    )

    # Getting the page source
    page_source = driver.page_source

    # Analyzing the page with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    categories_containers = re.findall(r'block block--category block--category\w* collapsible-nodes',
                                       str(soup.find(class_='p-body-pageContent')))
    # ПАРСИНГ ДАННЫХ О КАТЕГОРИЯХ
    for category in categories_containers:
        description = soup.find(class_=category).find(class_='block-desc').text \
            if soup.find(class_=category).find(class_='block-desc') else None
        name = soup.find(class_=category).find('a')
        id = re.findall(r'\d\d\d|\d\d|\d', category)[0]

        # чтение данных о саб формуах
        sub_forums_containers = re.findall(r'node node--id\w*',
                                       str(soup.find(class_=category).find(class_='block-container')))
        sub_forum_count = len(sub_forums_containers)
        sub_forums_id =''
        for sub_forum in sub_forums_containers:
            sub_forums_id += re.findall(r'\d\d\d|\d\d|\d', sub_forum)[0]
            sub_forums_id += '|'
        categories.append({
            'Id': id,
            'Name': name,
            'Description': description,
            'Sub_forum_count': sub_forum_count,
            'Sub_forum_id_list': sub_forums_id
        })
    print(categories)
    return categories
    # print(soup.findAll(class_=category))

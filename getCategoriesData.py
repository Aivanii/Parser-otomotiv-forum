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
    categories = [{
        'Id',
        'Name',
        'Description',
        'Sub_forum_count',
        'Sub_forum_id_list'
    }]
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

    for category in categories_containers:

        name = soup.find(class_=category).find('a')
        id = re.findall(r'\d\d\d|\d\d|\d', category)
        count = len(soup.find('block-container').find_all('div'))
        print(name.text, id, count)
       # print(soup.findAll(class_=category))


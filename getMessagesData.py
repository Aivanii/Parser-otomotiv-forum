from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options

# принмиает url на тему, а возвращает список со словорями 1 словарь -1 сообщение
def getAllMessage(url):
    # массив для сообщений
    messages = []
    # Navigating to the page
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=Options().add_argument("--disable-blink-features=AutomationControlled"))
    driver.get(url)

    # Ждем когда нужный нам элемент загрузится
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-template="thread_view"]'))
    )

    # Getting the page source
    page_source = driver.page_source

    # Analyzing the page with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    messages_containers = soup.find(class_='block-body js-replyNewMessageContainer').find_all('article')
    message_id_list = re.findall(r'post-\w*', str(messages_containers))
    print(message_id_list)
    for i in message_id_list:
        id = re.findall(r'\d\d\d\d\d\d', i)[0]
        print(id, 'id')
        print(soup.find(id = f"js-post-{id}").find( class_='message-userContent lbContainer js-lbContainer ').find(class_="bbWrapper") )
    #id_list = messages_containers.find_all('id')

    print(str(messages_containers))
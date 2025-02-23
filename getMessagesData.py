from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options
import requests
from pathlib import  Path

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

    # получаем id всех сообщений на форуме
    messages_containers = soup.find(class_='block-body js-replyNewMessageContainer').find_all('article')
    message_id_list = set(re.findall(r'post-\d+', str(messages_containers)))
    print(message_id_list)

    # получаем id форума
    forum_id = re.findall(r'\d+', str(soup.find(class_='block-container lbContainer')['data-lb-id']))[0]
    print(forum_id)

    for id in message_id_list:
        id_num = re.findall(r'\d+', id)[0] # численная часть id сообщения
        message = {} # словарь с инфой о сообщении

        # собираем все теги кроме дочерних, где содержится информация о сообщениях
        messages_info = soup.find_all(id=f"js-post-{id_num}")

        # добовляем чсиловой id сообщения в словарь
        message["message_id"] = id_num

        for message_info in messages_info: # пробегаемся по тегам содержащим ифнормацию о сообщении

            # получаем текст сообщения, без учета "овета"
            text = message_info.find('blockquote').nextSibling.strip() \
                if message_info.find('blockquote') \
                else message_info.find(class_="bbWrapper").find(class_="username--style5").parent.nextSibling.strip()\
                if message_info.find(class_="bbWrapper").find(class_="username--style5") \
                else message_info.find(class_="bbWrapper").text

            # получаем дату отправки сообщения
            date = message_info.find(class_="u-dt")['title']

            # получаем id отправителя
            user_id = message_info.find('a')['data-user-id']

            # получение ссылок из сообщения
            message_Urls = message_info.find(class_='bbWrapper').find_all(
                class_="link link--external fauxBlockLink-blockLink")
            Urls = []
            if message_Urls is not []: # првоеряем наличие ссылок
                for url in message_Urls:  # перебираем все ссылки из сообщения и форматируем их
                    if 'youtube.com' in url['href']:
                        continue
                    url = url['href'].replace('https://otomotiv-forum.com/', 'https://avtooblako.ru/')
                    Urls.append(url)
            else:
                Urls = None

            # получаем id сообщение на которое сделан овтет
            raw_reply_message_id = message_info.find('blockquote')['data-source'] if message_info.find('blockquote') else None
            # извлекаем численную часть из id
            replay_message_id = re.findall(r'\d+', str(raw_reply_message_id)) if raw_reply_message_id is not None else None

            # получаем id юзеров поставивших лайки
            reaction_data_url = f"https://otomotiv-forum.com/posts/{id_num}/reactions"# ссылка гнде хранится ифна о реакциях
            driver.get(reaction_data_url)# прогружаем новую страницу в драйвере
            users_reacted_page = BeautifulSoup(driver.page_source, 'html.parser')
            user_reacted_info_containers = users_reacted_page.find(class_='block-container')\
                .find_all(class_='block-row block-row--separated') \
                if users_reacted_page.find(class_='block-container') else []

            likes_user_id = '' # строка в которой будут хранится id юзеров
            for user_reacted_info in user_reacted_info_containers:

                likes_user_id += user_reacted_info.find('a')['data-user-id']
                likes_user_id += '|'

            # получаем id человека который упомянут в сообщении, если такой есть
            user_mention_id = message_info.find(class_="bbWrapper").find(class_="username--style5").parent['data-user-id']\
                if message_info.find(class_="bbWrapper").find(class_="username--style5") else None

            # локально сохраняем вложенные в сообщение файлы
            files_info = message_info.find_all(class_='file file--linked')\
                if message_info.find_all(class_='file file--linked')  else None
            file_paths = ''
            if files_info is not None:
                for file_info in files_info:
                    url = file_info.find("a", class_=lambda x: x and "file-preview" in x.split())
                    file_url =   f'https://otomotiv-forum.com{url["href"]}'
                    file_name = file_info.find(class_='file-name')['title']

                    output_dir = Path("data")  # Папка для сохранения файлов
                    output_dir.mkdir(exist_ok=True)  # Создаем папку если ее нет

                    filepath = f"{output_dir}/{file_name}"
                    def get_cookies_dict(driver):
                            """Преобразует cookies Selenium в словарь для requests."""
                            cookies = driver.get_cookies()
                            cookies_dict = {}
                            for cookie in cookies:
                                cookies_dict[cookie['name']] = cookie['value']
                            return cookies_dict
                    req = requests.get(file_url, cookies= get_cookies_dict(driver))
                    #print(req.content)
                    with open(filepath, "wb") as f:
                                f.write(req.content)
                    file_paths+=filepath
                    file_paths+='|'

            # сохраняем  данные в словарь
            message['date'] = date
            message["text"] = text
            message['user_id'] = user_id
            message['Urls'] = Urls
            message['forum_id'] = forum_id
            message['reply_message_id'] = replay_message_id
            message['likes_user_id'] = likes_user_id
            message['user_mention_id'] = user_mention_id
            message['path_files'] = file_paths

        messages.append(message)
    print(messages)
    # id_list = messages_containers.find_all('id')
    """{
        path_files,
        urls,
        date,
        text,
        id,
        likes_user_id,
        user_id,
        forum_id,
        reply_message_id,
        user_mention_id,
        
    }"""

    # print(str(messages_containers))

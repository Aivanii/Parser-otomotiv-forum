import random

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import requests
from pathlib import Path

def getUserDataByUrl(user_url, driver):
    # Navigating to the page
    driver.get(user_url)

    # Waiting for the <body data-template="member_view"> element to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-template="member_view"]'))
    )

    # Getting the page source
    page_source = driver.page_source

    # Analyzing the page with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extracting user ID from the URL
    id = None
    match = re.search(r'\.(\d+)', user_url)

    if match:
        id = match.group(1)
    # Extracting old username
    old_name = soup.find('span', class_='username--style5').text.strip() \
        if soup.find('span',class_='username--style5') else None
    # Generate name
    characters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._"  # Возможные символы
    name = ''.join(random.choice(characters) for _ in range(random.randint(3, 12)))

    # Extracting registration date
    registration_date = None
    registration_dd = soup.find('dt', string='Регистрация').find_next_sibling('dd')
    if registration_dd:
        registration_time = registration_dd.find('time')
        registration_date = registration_time.text.strip() if registration_time else None

    # Extracting message count
    message_count = soup.find('dl', class_='pairs pairs--rows pairs--rows--centered fauxBlockLink').find('dd').text.strip() if soup.find('dl', class_='pairs pairs--rows pairs--rows--centered fauxBlockLink') else None

    # Generate password
    password = ''
    for i in range(random.randint(5, 6)):
        password+= chr(random.randint(33, 125))
    # Extracting reaction count
    reaction_count = None
    reaction_dd = soup.find('dt', string='Реакции').find_next_sibling('dd')
    if reaction_dd:
        reaction_count = reaction_dd.text.strip()

    # Extracting last activity
    last_activity = None
    last_activity_dd = soup.find('dt', string='Последняя активность').find_next_sibling('dd')
    if last_activity_dd:
        last_activity_time = last_activity_dd.find('time')
        last_activity = last_activity_time.text.strip() if last_activity_time else None

    # Extracting status
    status = soup.find('span', class_='userTitle').text.strip() if soup.find('span', class_='userTitle') else None

    # Extracting role
    role = ''.join([banner.text.strip() for banner in soup.find_all('strong')]) if soup.find_all('strong') else None
    
    # Result output
    return({
        'ID': id,
        'Old_Name': old_name,
        'Name': name,
        'Password': password,
        'User_URL': user_url,
        'Registration_Date': registration_date,
        'Message_Count': message_count,
        'Reaction_Count': reaction_count,
        'Last_Activity': last_activity,
        'Status': status,
        'Role': role
    })


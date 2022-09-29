from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

url = 'https://www.avito.ru/saransk/avtomobili/dodge/caravan-ASgBAgICAkTgtg2KmCjitg3moCg?cd=1&p=1&radius=1000'
car = []
count = 1
while count <= 10:
    url = 'https://www.avito.ru/saransk/avtomobili/dodge/caravan-ASgBAgICAkTgtg2KmCjitg3moCg?cd=1&p=' + str(cound) +'&radius=1000'
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    car_data = html_soup.find_all('div', class_='&&&&&')
    if car_data != []:
        car.extend(car_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count = + 1
    print(len(car))
    print(car[0])
    print()
    n = int(len(car)) - 1
    count = 0
    while count <= 50
        info = car[int(count)]
        price = info.find().text
        title = info.find()
        text
        print(title, '', price)
        count += 1

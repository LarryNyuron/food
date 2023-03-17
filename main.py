import csv
import requests
import time
import random
import sys

from additional_functions import what_page
from bs4 import BeautifulSoup
from func_part_of_recipe import recipe_obj


base_url = 'https://eda.ru'
url = 'https://eda.ru/recepty?page=' 
i = '4069' 


response = requests.get(url + i)


f = open('recipes.txt', 'a')
while response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    all = soup.find_all('a', 'emotion-12sjte8')
    for a in all:
        f.write(a['href'] + '||| \n')
    what_page(i)
    i = str(int(i) + 1)
    response = requests.get(url + i) 
    time.sleep(random.randint(1, 5))
f.close()

    
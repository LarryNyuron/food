'''import csv
import requests
import aiohttp
import asyncio


from bs4 import BeautifulSoup
from additional_functions import what_page
from func_part_of_recipe import recipe_obj


BASE_URL = 'https://eda.ru/recepty?page='
NUM_PAGES = 3564
#Selectors for parsing
SELECTORS = {
    'title': {'selector': 'a', 'attr': 'emotion-12sjte8'},
}


#Sending requests and receiving (HTML code) page response
async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


#parses the elements on the page and returns a dictionary with the results
async def parse_page(session, url):
    html = await fetch_page(session, url)
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for element in soup.find_all('a', 'emotion-12sjte8'):
        item = []
        for a in element:
            item.append(a['href'] + ',n')
        results.append(item)
    return results


#parse all pages
async def parse_all_pages():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, NUM_PAGES + 1):
            url = f'BASE_URL}i}'
            tasks.append(asyncio.ensure_future(parse_page(session, url)))
        results = await asyncio.gather(*tasks)
    return [item for result in results for item in result]


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    items = loop.run_until_complete(parse_all_pages())
    f = open('recipes.txt', 'a')
    f.write(items)
    f.close()



Синхронно парсит
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
i = '68'


response = requests.get(url + i)


#The cycle by which the pages of each individual recipe are pulled out
f = open('recipes.txt', 'a')
while response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    all = soup.find_all('a', 'emotion-12sjte8')
    for a in all:
        f.write(a['href'] + ',\n')
    what_page(i)
    i = str(int(i) + 1)
    response = requests.get(url + i)
    time.sleep(random.randint(1, 5))
f.close()

'''

import csv
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
        item = {}
        for key, value in SELECTORS.items():
            selector = value['selector']
            attr = value['attr']
            elem = element.select_one(selector)
            item[key] = elem.get(attr) if elem else None
        results.append(item)
    return results


#parse all pages
async def parse_all_pages():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, NUM_PAGES + 1):
            url = f'{BASE_URL}{i}'
            tasks.append(asyncio.ensure_future(parse_page(session, url)))
        results = await asyncio.gather(*tasks)
    return [item for result in results for item in result]


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    items = loop.run_until_complete(parse_all_pages())
    f = open('recipes.txt', 'a')
    f.write(items)
    f.close()

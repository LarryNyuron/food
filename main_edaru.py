import csv
import time
import random
import sys
import asyncio
import aiohttp
from additional_functions import what_page
from bs4 import BeautifulSoup
from func_part_of_recipe import recipe_obj



'''
base_url = 'https://eda.ru'
i = '1'


response = requests.get(url + i)


#The cycle by which the pages of each individual recipe are pulled out
f = open('recipes.txt', 'a')
while response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    all = soup.find_all('a', 'emotion-18hxz5k')
    for a in all:
        f.write(a['href'] + ',\n')
    what_page(i)
    i = str(int(i) + 1)
    response = requests.get(url + i)
    time.sleep(random.randint(1, 5))
f.close()
'''


pages = [i for i in range(1, 5)]


async def get_link(session, page):
    url = 'https://eda.ru/recepty?page=' + str(page)

    async with session.get(url=url) as response:
        response_link = await response.text()
        soup = BeautifulSoup(response_link, 'html.parser')
        all = soup.find_all('a', 'emotion-18hxz5k')
        list_link = []
        for a in all:
            list_link.append(a['href'] + ',\n')
        f = open('recipes.txt', 'a')
        for i in list_link:
            f.write(i)
        f.close()

    print(f'[INFO] processed page {page}')


async def gather():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in pages:
            task = asyncio.create_task(get_link(session, page))
            tasks.append(task)

        await asyncio.gather(*tasks)



def main():
    asyncio.run(gather())


if __name__ == '__main__':
    f = open('recipes.csv', 'a')
    main()

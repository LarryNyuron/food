from xml.dom.minidom import Attr
from cv2 import exp
from numpy import short
import requests


from bs4 import BeautifulSoup


base_url = 'https://eda.ru'


def recipe_obj(part_url):
    soup = BeautifulSoup(requests.get(base_url + part_url).text, 'html.parser')
    return { 
        'title': recipe_title(soup),
        'portion': recipe_portion(soup),
        'time_for_preparing': time_for_preparing(soup),
        'number of additions to the recipe book': num_additions_to_recipebook(soup),
        'likes': num_of_likes(soup),
        'dislikes': num_of_dislikes(soup),
        'short_description': short_description(soup),
        'energy value per serving': {
            'calories': calories(soup),
            'proteins': proteins(soup),
            'fats': fats(soup),
            'carbohydrates': carbohydrates(soup),
        },
        'ingredients': ingredients(soup),
        'tags': tags_of_recipe(soup)
    }

def recipe_title(soup):
    try:
        return soup.find('h1', "emotion-gl52ge").get_text()
    except AttributeError:
        return soup.find('h1', "emotion-gl52ge")

def recipe_portion(soup):
    try:
        return soup.find('span',  attrs={'itemprop':'recipeYield'}).get_text()
    except AttributeError:
        return soup.find('span',  attrs={'itemprop':'recipeYield'})

def time_for_preparing(soup):
    try:
        return soup.find('div', "emotion-my9yfq").get_text()
    except AttributeError:
        return soup.find('div', "emotion-my9yfq")

def num_additions_to_recipebook(soup):
    try:
        return soup.find('span', "emotion-11wewbl").get_text()
    except AttributeError:
        return soup.find('span', "emotion-11wewbl")

def num_of_likes(soup):
    try:
        trash_likes = soup.find('div', "emotion-kbgujp").get_text()
        return trash_likes[0:len(soup.find('span', "emotion-1w5q7lf").get_text())]
    except AttributeError:
        return soup.find('div', "emotion-kbgujp")

def num_of_dislikes(soup):
    try: 
        trash_likes = soup.find('div', "emotion-kbgujp").get_text()
        return trash_likes[len(soup.find('span', "emotion-1w5q7lf").get_text()):]
    except AttributeError:
        return soup.find('div', "emotion-kbgujp")

def short_description(soup):
    try:
        return soup.find('span', 'emotion-1x1q7i2').get_text().replace('\xa0', ' ').replace('\n', ' ')
    except AttributeError:
        return soup.find('span', 'emotion-1x1q7i2')

def short_description(soup):
    try:
        return soup.find('span', 'emotion-1x1q7i2').get_text().replace('\xa0', ' ').replace('\n', ' ')
    except AttributeError:
        return soup.find('span', 'emotion-1x1q7i2')

def calories(soup):
    try:
        return soup.find('span', {'itemprop':'calories'}).get_text()
    except AttributeError:
        return soup.find('span', {'itemprop':'calories'})

def proteins(soup):
    try:
        return soup.find('span', {'itemprop':'proteinContent'}).get_text()
    except AttributeError:
        return soup.find('span', {'itemprop':'proteinContent'})

def fats(soup):
    try:
        return soup.find('span', {'itemprop':'fatContent'}).get_text()
    except AttributeError:
        return soup.find('span', {'itemprop':'fatContent'})

def carbohydrates(soup):
    try:
        return soup.find('span', {'itemprop':'carbohydrateContent'}).get_text()
    except AttributeError:
        return soup.find('span', {'itemprop':'carbohydrateContent'})

def ingredients(soup):
    try:
        return dict(zip(name_of_ingredients(soup), amount_of_ingredients(soup)))
    except AttributeError:
        return [name_of_ingredients(soup), amount_of_ingredients(soup)]

def name_of_ingredients(soup):
    try:
        return [ingredient.get_text() for ingredient in soup.find_all('span', {'itemprop':'recipeIngredient'})]
    except AttributeError:
        return soup.find_all('span', {'itemprop':'recipeIngredient'})

def amount_of_ingredients(soup):
    try:
        return [amount.get_text() for amount in soup.find_all('span', 'emotion-15im4d2')]
    except AttributeError:
        return soup.find_all('span', 'emotion-15im4d2')

def tags_of_recipe(soup):
    try:
        return [tags.get_text() for tags in soup.find_all('div', 'emotion-zwg7c9')]
    except AttributeError:
        return soup.find_all('div', 'emotion-zwg7c9')
    

#TODO изменить time_for_preparing для того, чтобы функция прив одила время к минутам
#TODO сделать функцию, которая вытаскивает инструкцию приготовления по-шагово и
#написать для нее функцию


if __name__ == "__main__":
    print(type(recipe_obj('/recepty/vypechka-deserty/brauni-brownie-20955')))
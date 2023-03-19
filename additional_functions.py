def what_page(num):
    print('Ok  page  #' + num)
    print('---' * 25)

'''def cast_in_minutes(time):
    if len(time)<=10:
        time=time[time.index('минут'):]
    elif

    with open('recipes.csv', 'w', newline='') as csvfile:

    fieldnames = ['title',
        'portion',
        'time_for_preparing',
        'number_of_additions_to_the_recipe_book',
        'likes',
        'dislikes',
        'short_description',
        'calories',
        'proteins',
        'fats',
        'carbohydrates',
        'ingredients',
        'tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'title':recipe_obj(a['href'])['title'],
                             'portion':recipe_obj(a['href'])['portion'],
                             'time_for_preparing':recipe_obj(a['href'])['time_for_preparing'],
                             'number_of_additions_to_the_recipe_book':recipe_obj(a['href'])['number of additions to the recipe book'] ,
                             'likes':recipe_obj(a['href'])['likes'],
                             'dislikes':recipe_obj(a['href'])['dislikes'],
                             'short_description':recipe_obj(a['href'])['short_description'],
                             'calories':recipe_obj(a['href'])['energy value per serving']['calories'],
                             'proteins':recipe_obj(a['href'])['energy value per serving']['proteins'],
                             'fats':recipe_obj(a['href'])['energy value per serving']['fats'],
                             'carbohydrates':recipe_obj(a['href'])['energy value per serving']['carbohydrates'],
                             'ingredients':recipe_obj(a['href']),
                             'tags':recipe_obj(a['href'])['tags']})

Не использовал сразу, потому что не хотел с этой ошибкой разбираться
UnicodeEncodeError: 'charmap' codec can't encode character '\xbd' in position 1554: character maps to <undefined>

                             '''

#TODO
# cast_in_minutes - для того, чтобы приводить значение времени готовки
# к минутам



if __name__ == "__main__":
    pass
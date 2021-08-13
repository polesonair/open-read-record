from pprint import pprint


# №1
def create_cook_book(input_file_name):
    cook_book = {}

    try:
        with open(input_file_name, encoding='utf-8') as f: # считали файл, разбили на строки, записали в список
            lst = [line.strip() for line in f]
        for i, j in enumerate(lst):
            if j.isdigit(): # метод для поиска числе, если перебираем число, то берем название предыдущего блюда
                cook_book[lst[i-1]] = [] # собираем их списк

                for s in lst[i+1:i+int(j)+1]:
                    ingredient_name = s.split('|')[0]
                    quantity = int(s.split('|')[1])
                    measure = s.split('|')[2]

                    cook_book[lst[i-1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {input_file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'


# №2
def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    ingredient_dict = {}

    for key in cooking_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    ingredient_name = dictionary['ingredient_name']

                    try:
                        ingredient_dict[ingredient_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ingredient_dict[ingredient_name] = {'measure': dictionary['measure'],
                                              'quantity': dictionary['quantity'] * person_count}

    return ingredient_dict

pprint(create_cook_book('recipes.txt'))
print ('----------------------------')
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], create_cook_book('recipes.txt'), 2))
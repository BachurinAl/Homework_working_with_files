from pprint import pprint


def recipes_file():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for recipe in file:
            dish = recipe.strip()
            count = int(file.readline().strip())
            temp = []
            for ingredients in range(count):
                i, q, m = file.readline().split(' | ')
                temp.append({'ingredient_name': i, 'quantity': int(q), 'measure': m.strip()})
            cook_book[dish] = temp
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredients in recipes_file()[dish]:
            if ingredients["ingredient_name"] in shop_list:
                shop_list[ingredients["ingredient_name"]]["quantity"] += ingredients["quantity"] * person_count
            else:
                shop_list[ingredients["ingredient_name"]] = {"measure": ingredients["measure"], "quantity": ingredients["quantity"] * person_count}
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

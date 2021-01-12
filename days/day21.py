import copy

with open("inputs/input21.txt", "r") as f:
    lines = f.read().splitlines()

items = []

for l in lines:
    items.append([i.split() for i in l.split("(")])
    items[-1][0] = set(items[-1][0])
    items[-1][1] = [i.replace(")", "").replace(",", "") for i in items[-1][-1]]
    items[-1][1] = set([i for i in items[-1][-1] if not i == "contains"])

allergens = set()
ingredients = set()

for i in items:
    allergens = allergens | i[1]
    ingredients = ingredients | i[0]

open_items = copy.deepcopy(items)
open_allergens = copy.deepcopy(allergens)
remaining_not_final = True
safe_ingreds = copy.deepcopy(ingredients)


def find_possible(items, allergen, ingredients):
    possible_ingred = copy.deepcopy(ingredients)
    for i in items:
        if a in i[1]:
            possible_ingred = possible_ingred & i[0]
    return possible_ingred


def remove_pair(items, allergen, ingred):
    new_items = []
    print(f"removing {allergen} {ingred}")
    for i in items:
        new_item = [
            set([j for j in i[0] if not j == ingred]),
            set([j for j in i[1] if not j == allergen]),
        ]
        if new_item[1] and new_item[0]:
            new_items += new_item
    print(new_items[:5])
    print(items[:5])
    return new_items


while remaining_not_final:
    remaining_not_final = False
    for a in open_allergens:
        possible_ingred = find_possible(open_items, a, ingredients)
        if len(possible_ingred) == 1:
            open_allergens_new = open_allergens - set([a])
            open_items = remove_pair(open_items, a, list(possible_ingred)[0])
            remaining_not_final = True
            safe_ingreds = safe_ingreds - possible_ingred
    open_allergens = open_allergens_new
    if not open_allergens:
        remaining_not_final = False


for a in open_allergens:
    possible_ingred = find_possible(open_items, a, ingredients)
    safe_ingreds = safe_ingreds - possible_ingred

count = 0
for i in safe_ingreds:
    for j in items:
        if i in j[0]:
            count += 1

print(count)
print(open_allergens)
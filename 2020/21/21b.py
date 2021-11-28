import fileinput
import re


def parse_input():
    examples = [x.strip() for x in fileinput.input()]
    foods_with_allergens = []
    for example in examples:
        matched = re.search(r'(?P<food>(\w+\s)+)\(contains (?P<alergens>(\w+)(, \w+)*)\)', example)
        food = matched.group("food").split()
        alergen = set(matched.group("alergens").split(", "))
        foods_with_allergens.append((alergen, food))
    return foods_with_allergens


def get_all_allergens(foods):
    allergens = set()
    for alls, _ in foods:
        for allergen in alls:
            allergens.add(allergen)
    allergens = list(allergens)
    return allergens


def check_food(allergens, foods):
    for allergen in allergens:
        if allergen in matches:
            return
        else:
            matching = []
            for all, food in foods:
                if allergen in all:
                    matching.append(set(food))
            res = set.intersection(*matching)
            if len(res) == 1:
                res = res.pop()
                matches[allergen] = res
                erase_food_from_list(res, foods)
                allergens.remove(allergen)
                return check_food(allergens, foods)
            else:
                continue


def erase_food_from_list(to_erase, foods):
    for _, food in foods:
        if to_erase in food:
            food.remove(to_erase)


foods_with_allergens = parse_input()
allergens = get_all_allergens(foods_with_allergens)

matches = {}
check_food(allergens, foods_with_allergens)

sorted_alphabetically = dict(sorted(matches.items()))
values = []
for value in sorted_alphabetically.values():
    values.append(value)

result = ",".join(values)
print(result)

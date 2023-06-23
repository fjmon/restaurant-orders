import csv
from models.dish import Dish, Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as file:
            csv_file = csv.reader(file)
            header, *data = csv_file
            all_dish_set = {}
            for line in data:
                dish = line[0]
                price = float(line[1])
                ingredient_type = line[2]
                quantity = int(line[3])
                if dish not in all_dish_set:
                    all_dish_set[dish] = Dish(dish, price)
                dish = all_dish_set[dish]
                ingredient = Ingredient(ingredient_type)
                dish.add_ingredient_dependency(ingredient, quantity)

            self.dishes = set(all_dish_set.values())

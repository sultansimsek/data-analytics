fav_foods = ["dolma", "sushi", "salad", "tantuni", "ramen"]
for index, food in enumerate(fav_foods, start=1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")

for index, food in enumerate(reversed(fav_foods), start=1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")
class Restaurant:
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

mcdonalds  = Restaurant("McDonald's",     "American fast food")
taco_bell  = Restaurant("Taco Bell",      "Mexican-inspired fast food")
dunkin     = Restaurant("Dunkin' Donuts", "coffee and donuts")

mcdonalds.describe_rest()
mcdonalds.rest_open()

taco_bell.describe_rest()
taco_bell.rest_open()

dunkin.describe_rest()
dunkin.rest_open()
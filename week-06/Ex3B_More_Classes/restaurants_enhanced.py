class Restaurant:
    
    def __init__(self, rest_name, food_type):
        self.rest_name      = rest_name
        self.food_type      = food_type
        self.number_served  = 0
        self.customer_ratings = []      # fresh list per instance

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    


    def add_num_served(self):
        served = int(input("How many customers served today? "))
        self.number_served += served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            raw = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")
            try:
                rating = int(raw)        
                if 1 <= rating <= 5:
                    break               
                else:
                    print("Please enter a whole number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a whole number between 1 and 5.")

        self.customer_ratings.append(rating)
        avg = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for {self.rest_name} is {avg:.1f}.")


mcdonalds = Restaurant("McDonald's",     "American fast food")
taco_bell = Restaurant("Taco Bell",      "Mexican-inspired fast food")
dunkin    = Restaurant("Dunkin' Donuts", "coffee and donuts")

mcdonalds.print_num_served()
taco_bell.print_num_served()
dunkin.print_num_served()

mcdonalds.number_served += 120
mcdonalds.number_served += 85
taco_bell.number_served += 200
dunkin.number_served    += 310


mcdonalds.print_num_served()
taco_bell.print_num_served()
dunkin.print_num_served()


def simulate_rating(restaurant, raw_input):
    try:
        rating = int(raw_input)
        if 1 <= rating <= 5:
            restaurant.customer_ratings.append(rating)
            avg = sum(restaurant.customer_ratings) / len(restaurant.customer_ratings)
            print(f"Your rating was {rating}. The average rating for {restaurant.rest_name} is {avg:.1f}.")
        else:
            print(f"Input '{raw_input}': out of range — please enter 1 to 5.")
    except ValueError:
       print(f"Input '{raw_input}': invalid — please enter a whole number 1-5.")

# Valid ratings
simulate_rating(mcdonalds, "4")
simulate_rating(mcdonalds, "3")
simulate_rating(mcdonalds, "5")

# Step 6c — bad inputs
simulate_rating(mcdonalds, "6")        # out of range integer
simulate_rating(mcdonalds, "2.5")     # decimal — int() raises ValueError
simulate_rating(mcdonalds, "5 stars!") # non-numeric string — int() raises ValueError
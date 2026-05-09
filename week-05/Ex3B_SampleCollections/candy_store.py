#Start by creating two tuples: one that lists at least 3 types of candy that can come in fruit flavors, and another that lists at least 3 fruity flavors. 
candy = ("Skittles", "Haribo", "Welch's")
flavors = ("Strawberry", "Coke", "Orange")
#Now create a new variable to store candy combinations as a set. Using the index of each tuple, add at least one combination of each candy and flavor to the new set – for example, putting together tuple1[0] and tuple2[1
candy_combinations = set()
candy_combinations.add(candy[0] + " " + flavors[0])
candy_combinations.add(candy[1] + " " + flavors[1])
candy_combinations.add(candy[2] + " " + flavors[2])
print(candy_combinations)   
print(f"Today's candy options include:{candy_combinations}.")
#What I have realised in this exercise is that sets are unordered collections of unique elements, so the order of the combinations in the set may not be the same as the order in which they were added. 

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00
total_due = food_cost + tax + tip
print("The total due is: $" + str(total_due))
# We use string function to concatanate the string with the total due, which is a number. We need to convert it to a string first before concatenating.
print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Total due is " + str(total_due))
print("Tip is $" + format(tip, ".2f"))
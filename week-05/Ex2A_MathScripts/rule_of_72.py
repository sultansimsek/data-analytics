savings = 2000
interest_rate = 0.05
years_to_double = 72 / (interest_rate * 100)

print("Your current savings is " + str(savings) + "." )
print("At an interest rate of " + str(interest_rate) + "%, your savings account will be worth " + format(savings * 2, ".2f") + " in " + str(years_to_double) + " years for your savings to double.") 
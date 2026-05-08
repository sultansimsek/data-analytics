print("""There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
$250 per day to rent (including the driver’s pay). How many vans do you need? How
much will it cost to rent vans? What is the cost if you split it per person?""")
people = int(input("Enter the number of people going on the tour: "))
vans_needed = (people + 14) // 15  # This ensures we round
total_cost = vans_needed * 250
cost_per_person = total_cost / people
print(f"You need {vans_needed} vans to accommodate {people} people.")
print(f"The total cost to rent the vans is: ${format(total_cost, '.2f')}") 
print(f"The cost per person is: ${format(cost_per_person, '.2f')}")
#a) How much money did your script say you had to charge per person? $19.75
#b) If you multiply that out, how much did you collect? $19.75 * 40 = $790
#c) How much were the vans? $250 * 3 = $750
#d) Why do you have leftover money? Because we rounded up the number of vans needed, we ended up renting 3 vans instead of 2, which increased the total cost. The extra money collected from the people is due to the additional van that was rented to accommodate everyone.
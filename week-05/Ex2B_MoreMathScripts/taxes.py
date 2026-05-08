print("Federal taxes are 23% of your salary every month. You make X amount of money. How much is withheld for taxes?")
salary = float(input("Enter your monthly salary: "))
taxes_withheld = salary * 0.23
print(f"The amount withheld for taxes is: {format(taxes_withheld, '.2f')}")

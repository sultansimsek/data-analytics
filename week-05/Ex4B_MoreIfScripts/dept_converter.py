#use if/elif/else logic to determine and print department name based on a department code. Make sure to test your script with multiple codes, 1 Marketing5 Human Resources, 10 Accounting, 12 Legal, 18 IT, 20 Customer Relation
code = int(input("Enter the department code: "))
if code == 1:
    print("Marketing")
elif code == 5:
    print("Human Resources")
elif code == 10:
    print("Accounting")
elif code == 12:
    print("Legal")
elif code == 18:
    print("IT")
elif code == 20:
    print("Customer Relation")
else:    print("Invalid department code")
#
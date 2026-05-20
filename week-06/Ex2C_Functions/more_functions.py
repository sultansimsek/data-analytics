def display_mailing_label(name, address, city, state, zip):
    print(f"-------------------------")
    print(f"  {name}")
    print(f"  {address}")
    print(f"  {city}, {state} {zip}")
    print(f"-------------------------")


display_mailing_label("Maria Garcia", "123 Maple St", "Chicago", "IL", "60601")

display_mailing_label("James Wilson", "456 Oak Ave", "Atlanta", "GA", "30301")

def add_numbers(*args):
    result = sum(args)
    equation = " + ".join(str(n) for n in args)
    print(f"{equation} = {result}")

# One number
add_numbers(5)
# Two numbers
add_numbers(10, 20)
# More than two numbers
add_numbers(3, 7, 12, 8, 5)

def display_receipt(total_due, amount_paid):
    print(f"Total Due:    ${total_due:.2f}")
    print(f"Amount Paid:  ${amount_paid:.2f}")
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due:   ${change:.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Balance Due:  ${balance:.2f} — payment incomplete")
    print()

# Overpay
display_receipt(45.00, 60.00)
# Exact pay
display_receipt(32.50, 32.50)
# Underpay
display_receipt(78.99, 50.00)


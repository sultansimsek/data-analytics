pay_rate = float(input("Enter the pay rate: "))
hours_worked = float(input("Enter the hours worked: "))
overtime_hours = hours_worked - 40 
overtime_pay = pay_rate * 1.5
gross_pay = hours_worked * pay_rate
reason = ["Under 40 hours", "Exactly 40 hours","Over 40 hours"]

if hours_worked > 40:
    gross_pay = (40 * pay_rate) + (overtime_hours * overtime_pay)
    print(f"When the pay rate is ${pay_rate} and the hours worked is {hours_worked}, the gross pay is ${gross_pay} because the employee worked {reason[2]}.")
elif hours_worked == 40:
    print(f"When the pay rate is ${pay_rate} and the hours worked is {hours_worked}, the gross pay is ${gross_pay} because the employee worked {reason[1]}.")
else:
    print(f"When the pay rate is ${pay_rate} and the hours worked is {hours_worked}, the gross pay is ${gross_pay} because the employee worked {reason[0]}.")

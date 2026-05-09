pay_rate = float(input("Enter the pay rate: "))
hours_worked = float(input("Enter the hours worked: "))
overtime_hours = hours_worked - 40 
overtime_pay = pay_rate * 1.5
weekly_gross_pay = hours_worked * pay_rate
annual_salary = weekly_gross_pay * 52
filing_status = input("Enter your filing status (single, joint): ")
if filing_status == "single" and annual_salary < 12000:
    tax_rate = 0.05
elif filing_status == "single" and annual_salary >= 12000 and annual_salary < 25000:
    tax_rate = 0.10
elif filing_status == "single" and annual_salary >= 25000 and annual_salary < 75000:
    tax_rate = 0.15
elif filing_status == "single" and annual_salary >= 75000:
    tax_rate = 0.20
elif filing_status == "joint" and annual_salary < 12000:
    tax_rate = 0
elif filing_status == "joint" and annual_salary >= 12000 and annual_salary < 25000:
    tax_rate = 0.06
elif filing_status == "joint" and annual_salary >= 25000 and annual_salary < 75000:
    tax_rate = 0.11
elif filing_status == "joint" and annual_salary >= 75000:
    tax_rate = 0.20

print(f"You worked {hours_worked} hours this period. \n Because you earn ${pay_rate} per hour, your gross weekly pay is ${weekly_gross_pay}. \n Your filing status is {filing_status}. \n You witheld ${weekly_gross_pay * tax_rate} in taxes this week. \n Your net weekly pay is ${weekly_gross_pay - (weekly_gross_pay * tax_rate)}.")
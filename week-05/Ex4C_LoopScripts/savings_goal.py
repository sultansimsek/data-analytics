bank_bal = int(input("How much money do you have in the bank? "))
savings_goal = int(input("What is your savings goal? "))
weekly_savings = int(input("How much money can you save each week? "))
treat_cost = 10
while bank_bal < savings_goal:
    bank_bal += weekly_savings

     # 4b) Check for 75% progress first
    if bank_bal >= (savings_goal * 0.75):
        bank_bal -= treat_cost
        print(f"So close! After treating myself, my balance is up to {bank_bal}.")
        
    # 4a) Check for 50% progress (Halfway)
    elif bank_bal > (savings_goal / 2):
        print(f"Almost there! This week my balance is up to {bank_bal}.")
        
    # 3) Standard weekly update
    else:
        print(f"This week my balance increased to {bank_bal}.")

# 3) Final message once loop ends
print(f"Goal met! My current balance is {bank_bal}.")   
    
#What we realised is when we did the 50% progress check first, we never got to the 75% progress check because the 50% check was true for all values above 50%. By switching the order of the checks, we can ensure that we check for 75% progress first, and only if that is not true do we check for 50% progress.


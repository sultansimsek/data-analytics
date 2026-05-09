current_time = float(input("What time is it? (0-23) "))
if current_time < 10:
    print("Good morning!")
elif current_time >= 10 and current_time < 17:
    print("Good day!")
elif current_time >= 17:
    print("Good evening!")
elif current_time >= 23 or current_time < 4:
    print("What are you doing up so late?")
else:
    print("Invalid time entered. Please enter a number between 0 and 23.")  

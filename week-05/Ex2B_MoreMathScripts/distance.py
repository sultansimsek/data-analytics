print("How do you calculate the distance between coordinates (x1, y1) and (x2, y2)?")
import math
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between the two points is: {format(distance, '.2f')}")     
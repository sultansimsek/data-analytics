import random
import math
import statistics
vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi


#Experimenting with a subset of integers 1-100:

#Sum of 75 sample values from 1 to 100: ____
print("Sum of 75 sample values from 1 to 100:",
      sum(vals_sample))
#Average of 75 sample values: ____
print("Average of 75 sample values:",
      statistics.mean(vals_sample))
#Median of 75 sample values: ____
print("Median of 75 sample values:",
      statistics.median(vals_sample))
#_Experimenting with a superset of 200 values, integers 1-100:

#Average of 200 values: ____
print("Average of 200 values:",
      statistics.mean(vals_choices))
#Median of 200 values: ____
print("Median of 200 values:",
      statistics.median(vals_choices))
#Mode of 200 values: ____
print("Mode of 200 values:",
      statistics.mode(vals_choices))
#Standard deviation of 200 values: ____
print("Standard deviation of 200 values:",
      statistics.stdev(vals_choices))
#Variance of 200 values: ____
print("Variance of 200 values:",
      statistics.variance(vals_choices))
#_Modeling a random circle:
area = pi * radius ** 2
#Radius = __, area = ____ (rounded up to the nearest integer)
print(f"Radius = {radius}, \n area = {math.ceil(area)} (rounded up)")
#Radius = __, area = ____ (rounded down to the nearest integer)
print(f"Radius = {radius}, \n area = {math.floor(area)} (rounded down)")


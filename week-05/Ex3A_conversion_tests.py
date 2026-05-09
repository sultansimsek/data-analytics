# Description: This script tests various numeric
#              conversion techniques
# Author: Sultan Simsek
# The following variables are defined for testing
#a = " 101.1 " string
#b = '55' string
#c = "402 Stevens" string
#d = 'Number 5 ' string

a = int(float(" 101.1 ")) 
b = int('55') 
c = str("402") + ' Stevens'
d = int('5') 
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print ("There are " + c[0:3] + " people in the line to stadium")
#For variables a and d, use the .strip() method to remove the leading/trailing spaces, within a print statement to display each result.
print("The value of a is: " + str(a).strip())
print("The value of d is: " + str(d).strip())
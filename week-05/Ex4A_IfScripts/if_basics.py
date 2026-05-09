x = 100
y =20
#If x divided by y is 5, print “x divided by y is 5” and set the value of x to 1 – otherwise print “are the variables set up correctly?”
if x // y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("Are the variables set up correctly?")

if x*y == y:
    print("Now x times y is y")
    x = 10
else:  print("Whoops, x equals" + str(x))

if x<y:
    print("x is less than y")
    x = 2*x
else: print("uh oh x is not less than y")

print("The final value of x is: " + str(x))


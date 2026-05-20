# Step 2: create the lambda variable
doubler = lambda n: n * 2

# Step 3: test with three values
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Step 4: tripler using same lambda logic
tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# Step 5: factory function — returns a lambda, not a value
def multiplier(factor):
    return lambda n: n * factor

# Create one variable per factor using the factory
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler  = multiplier(6)
septupler  = multiplier(7)
octupler   = multiplier(8)
nonupler   = multiplier(9)
decupler   = multiplier(10)

print(f"quadrupler(5)  = {quadrupler(5)}")
print(f"quintupler(5)  = {quintupler(5)}")
print(f"sextupler(5)   = {sextupler(5)}")
print(f"septupler(5)   = {septupler(5)}")
print(f"octupler(5)    = {octupler(5)}")
print(f"nonupler(5)    = {nonupler(5)}")
print(f"decupler(5)    = {decupler(5)}")
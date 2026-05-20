try:
    result = int("hello")
except ValueError:
    print("ValueError: 'hello' cannot be converted to an integer.")
else:
    print(f"Converted successfully: {result}")
finally:
    print("Let's try another one...\n")

# Way 2: int() can't convert a float string
try:
    result = int("3.14")
except ValueError:
    print("ValueError: '3.14' is a float string — use float() first, then int().")
else:
    print(f"Converted: {result}")
finally:
    print("Let's try another one...\n")




# Way 1: assign an undefined variable
try:
    m = banana
except NameError:
    print("NameError: 'banana' is not defined — did you forget quotes?")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# Way 2: call a function that doesn't exist
try:
    total = add_numbers(5, 10)
except NameError:
    print("NameError: 'add_numbers' is not defined in this scope.")
else:
    print(f"Total: {total}")
finally:
    print("Let's try another one...\n")


# Way 1: can't add a string and an integer
try:
    result = "age: " + 25
except TypeError:
    print("TypeError: can't concatenate str and int — use str(25) first.")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# Way 2: calling a non-callable (an integer) as if it's a function
try:
    x = 5
    x(10)
except TypeError:
    print("TypeError: 'int' object is not callable — x is a number, not a function.")
else:
    print(x)
finally:
    print("Let's try another one...\n")

# Way 1: compile() a string containing invalid syntax
try:
    compile("if True print('hello')", "<string>", "exec")
except SyntaxError as e:
    print(f"SyntaxError: {e} — missing colon after 'if True'.")
else:
    print("Code compiled successfully.")
finally:
    print("Let's try another one...\n")

# Way 2: eval() a string with a syntax mistake
try:
    eval("x = = 5")
except SyntaxError as e:
    print(f"SyntaxError: {e} — double '=' is invalid; use '==' for comparison.")
else:
    print("No error.")
finally:
    print("Let's try another one...\n")
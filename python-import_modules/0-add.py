import importlib

# Assign values to a and b
a = 1
b = 2

# Import the add function from add_0.py
add_module = importlib.import_module('add_0')
add = add_module.add

# Calculate the result using the imported add function
result = add(a, b)

# Print the result with string formatting
print(f"{a} + {b} = {result}")


# import math_operations module
# - math_operations module will be searched in the current directory
# - this will import all the units (variable/function etc) from the module
# - to access any unit from the module, use the module name with dot operator
# - e.g. <modulename>.<function name>()
# - when a module is getting imported, all the statements in the module
#   will get executed


import math_operations

# call the add function from math_operations module
math_operations.add(40, 60)

# call the subtract function from math_operations module
math_operations.subtract(40, 60)

# call the divide function from math_operations module
math_operations.divide(40, 60)

# call the multiply function from math_operations module
math_operations.multiply(40, 60)

# access the PI constant from math_operations module
print(f"PI = {math_operations.PI}")

print(f"name of the program1 module = {__name__}")

# find the members of math_operations
print(dir(math_operations))
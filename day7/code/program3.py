# import only required members of the module
# - still the entire module will get loaded in the memory
# - all the lines from the module will get executed

# import add function from math_operations module
from math_operations import add

# import subtract function from math_operations module
from math_operations import subtract

# import divide, multiply and PI from math_operations module
from math_operations import divide, multiply, PI

add(40, 60)
subtract(40, 60)
divide(40, 60)
multiply(40, 60)
print(f"PI = {PI}")

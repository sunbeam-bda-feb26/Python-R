# import member from a module with an alias
# alias: temporary name given to the member

from math_operations import add as mo_add

# called from math_operations
mo_add(70, 80)

def add(p1: int, p2: int):
    print("called from program4 module")
    print(f"{p1} + {p2} = {p1 + p2}")

# called from program4
add(30, 40)

# called from math_operations
mo_add(60, 90)
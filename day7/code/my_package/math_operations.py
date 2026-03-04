# module
# - a file with .py (python code) or .pyc (byte codes) extesion
# - collection of variables/constants/functions/classes
# - basic unit of code sharing
# - injects an variable named __name__ in every module to identify the name of the module
# - the current running module will always have the name as __main__
# - the module which is being imported will always have the name same as the 
#   module file name
# - types
#   - system modules
#     - modules implemented by python
#     - get installed while installing python
#   - user defined module
#     - implemented by user
#     - need to be installed using any package manager
#     - e.g. math_operations
#     - third party modules
#       - modules implemented by other developers/communities
#       - e.g. numpy, pandas, matplotlib, seaborn etc.
# - package
#   - collection of modules in a directory with __init__.py file

# define a constant
PI = 3.14

def add(p1: int, p2: int):
    print(f"called from math_operations module")
    print(f"{p1} + {p2} = {p1 + p2}")

def subtract(p1: int, p2: int):
    print(f"called from math_operations module")
    print(f"{p1} - {p2} = {p1 - p2}")

def divide(p1: int, p2: int):
    print(f"called from math_operations module")
    print(f"{p1} / {p2} = {p1 / p2}")

def multiply(p1: int, p2: int):
    print(f"called from math_operations module")
    print(f"{p1} * {p2} = {p1 * p2}")

def square(n: int):
    print(f"called from math_operations module")
    print(f"square of {n} = {n ** 2}")

# print(f"name of math_operations module = {__name__}")

# NOTE: this is NOT a entry point function of python program
# - there is NO entry point function for any python program
# - the code starts its execution from line1, top to bottom
# - but the python virtual machine has got an entry point function __PyMain

# check if this module is being executed
# - if this module is getting executed, __name__ = '__main__'
# - if tihs module is being imported by others, __name__ = 'math_operations'
if __name__ == '__main__':
    add(10, 20)
    subtract(10, 20)
    divide(10, 20)
    multiply(10, 20)
    square(4)

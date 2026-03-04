# broadcasting operation
# - the operation will be performed on every element of the array
# - type
#   - arithemetic
#   - comparison
# filtering the values


import numpy as np

def function1():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers        = {numbers}")

    # [210, 220, 230, 240, 250]
    # [200 + n for n in numbers]
    print(f"numbers + 200  = {numbers + 200}")
    print(f"numbers - 5    = {numbers - 5}")
    print(f"numbers / 2    = {numbers / 2}")
    print(f"numbers // 2   = {numbers // 2}")
    print(f"numbers * 2    = {numbers * 2}")
    print(f"numbers ** 2   = {numbers ** 2}")

# function1()

def function2():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers        = {numbers}")

    print(f"numbers >  20  = {numbers > 20}")
    print(f"numbers <  20  = {numbers < 20}")
    print(f"numbers >= 20  = {numbers >= 20}")
    print(f"numbers <= 20  = {numbers <= 20}")
    print(f"numbers == 20  = {numbers == 20}")
    print(f"numbers != 20  = {numbers != 20}")

# function2()

def function3():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers          = {numbers}")

    # find the numbers less than 40
    # [n for n in numbers if n < 40]
    print(f"numbers < 40     = {numbers[numbers < 40]}")
    print(f"numbers < 40     = {numbers[[True, True, True, False, False]]}")

# function3()

def function4():
    # array of salaries
    salaries = np.array([30, 40, 35, 60, 80, 70, 90])
    print(f"salaries       = {salaries}")

    # find the salaries >= 60
    print(f"salaries >= 60 = {salaries[salaries >= 60]}")

# function4()

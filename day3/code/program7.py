# list
# - collection of similar or dissimilar values
# - iterate over a collection
#   - for..in loop
#     - preferred when the number of iterations is already known
#     - syntax: for <temporary variable> in <collection>: 
#     - by default
#       - starts from 0th position of collection
#       - ends at the last position of collection
#   - while loop
#     - preferred when the number of interations is NOT known
# - operations
#   - len(): used to get the length of a list
#   - 

def function1():
    # empty list
    empty_list = []
    print(f"empty_list = {empty_list}, type = {type(empty_list)}")

    # empty list
    empty_list = list([])
    print(f"empty_list = {empty_list}, type = {type(empty_list)}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers       = {numbers}, type = {type(numbers)}")

    # list of strings 
    countries = ["india", "usa", "uk", "japan", "bhutan"]
    print(f"countries     = {countries}, type = {type(countries)}")

    # list of boolean values
    statuses = [True, False, False, True, True]
    print(f"statuses      = {statuses}, type = {type(statuses)}")

    # list of mixed values
    mixed_values = [100, "india", 56.70, True, False, 20 + 5j, "usa"]
    print(f"mixed_values  = {mixed_values}, type = {type(mixed_values)}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers                 = {numbers}")

    # get the length of list
    print(f"no of values in numbers = {len(numbers)}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"length of numbers = {len(numbers)}")

    # iterate over the list using for..in loop
    for number in numbers:
        print(f"number = {number}")

    print('-' * 80)

    # list of strings
    countries = ["india", "usa", "uk", "japan", "bhutan"]
    print(f"length of countries = {len(countries)}")

    # iterate over the countries collection
    for country in countries:
        print(f"country = {country}")

# function4()

def function5():
    def add(p1: int, p2: int):
        return p1 + p2
    
    def subtract(p1: int, p2: int):
        return p1 - p2
    
    multiply = lambda p1, p2: p1 * p2
    divide = lambda p1, p2: p1 / p2

    # list of functions
    functions = [add, subtract, multiply, divide]

    # iterate over the collection and call every function
    for function in functions:
        # call the function
        print(f"result = {function(10, 20)}")

function5()
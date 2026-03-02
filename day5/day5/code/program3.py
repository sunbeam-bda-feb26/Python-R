# frozenset
# - unordered immutable collection of unique values

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50] 
    print(f"numbers_list         = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
    print(f"numbers_tuple        = {numbers_tuple}, type = {type(numbers_tuple)}")

    # mutable set of numbers
    numbers_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers_set          = {numbers_set}, type = {type(numbers_set)}")

    # immutable set of numbers
    numbers_frozen_set = frozenset([10, 20, 30, 40, 50, 10, 20, 30, 40, 50])
    print(f"numbers_frozen_set   = {numbers_frozen_set}, type = {type(numbers_frozen_set)}")

# function1()

def function2():
    # frozenset of numbers
    numbers = frozenset([10, 20, 30, 40, 50, 10, 20, 30, 40, 50])
    print(f"numbers    = {numbers}, type = {type(numbers)}")

    # add a number: is not possible as it is a immutable collection
    # numbers.add(60)
    # print(f"numbers    = {numbers}, type = {type(numbers)}")

    # remove a value: is not possible as it is a immutable collection
    # numbers.remove(40)
    # print(f"numbers    = {numbers}, type = {type(numbers)}")

# function2()

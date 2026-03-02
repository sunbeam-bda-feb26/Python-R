# set
# - mutable collection of unique values
# - unordered collection: the insertion order is not maintained
#   - the order in which the values stored internally is not same as insertion order
#   - set uses a hash function to decide the index position of the values
#   - values can NOT be retrieved using subscript or index positions
#   - indexing (positive or negative) is NOT supported in case of set
# - methods
#   - add(): 
#     - inserts a new value dynamically
#     - the index is controlled by the hash function used by the set
#   - remove():
#     - removes a value by using the 'value' and not by the index position
#   - clear():
#     - remove all the values from the set
#   - intersection():
#     - returns a set with common elements between two sets
#     - associative: s1.intersection(s2) == s2.intersection(s1)
#   - union()
#     - returns a set with all values from bothe sets
#     - but the commons elements will be kept only once
#     - associative: s1.union(s2) == s2.union(s1)
#   - subtraction
#     - returns a set with uncommon values from the first set
#     - not associative: s1 - s2 != s2 - s1


def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50] 
    print(f"numbers_list  = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")

    # set of numbers
    numbers_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers_set   = {numbers_set}, type = {type(numbers_set)}")

# function1()

def function2():
    # set of numbers
    numbers = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers    = {numbers}, type = {type(numbers)}")

    # read value at 0th index
    # this is NOT supported as set is a unordered collection
    # print(f"numbers[0] = {numbers[0]}")

    # get all the values from set
    for number in numbers:
        print(f"number = {number}")

# function2() 

def function3():
    # set of numbers
    numbers = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers    = {numbers}, type = {type(numbers)}")

    # add a number
    numbers.add(60)
    print(f"numbers    = {numbers}, type = {type(numbers)}")

    # add a number
    numbers.add(70)
    print(f"numbers    = {numbers}, type = {type(numbers)}")

# function3()


def function4():
    # set of numbers
    numbers = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers    = {numbers}, type = {type(numbers)}")

    # remove a value
    numbers.remove(40)
    print(f"numbers    = {numbers}, type = {type(numbers)}")

    # remove all the values
    numbers.clear()
    print(f"numbers    = {numbers}, type = {type(numbers)}")

# function4()

def function5():
    # set of numbers
    s1 = {10, 20, 30, 40, 50}
    s2 = {40, 50, 60, 70, 80}

    print(f"s1 = {s1}, s2 = {s2}")
    print(f'-' * 80)

    # intersection 
    print(f"s1.intersection(s2) = {s1.intersection(s2)}")
    print(f"s2.intersection(s1) = {s2.intersection(s1)}")
    print(f'-' * 80)

    # union
    print(f"s1.union(s2)        = {s1.union(s2)}")
    print(f"s2.union(s1)        = {s2.union(s1)}")
    print(f'-' * 80)

    # subtraction
    print(f"s1 - s2             = {s1 - s2}")
    print(f"s2 - s1             = {s2 - s1}")
    print(f'-' * 80)

# function5()

def function6():
    # list of person names
    names = ["steve", "steve", "steve", "bill", "bill", "john", "jane", "linda"]
    print(f"name              = {names}")

    # find the unique names from the list of names
    unique_names = []
    for name in names:
        # check if name is already present in unique_names list
        if name not in unique_names:
            unique_names.append(name)

    # print all the unique names
    print(f"unique names      = {unique_names}")
    print('-' * 80)
    
    # find the unique names from the list of names
    # convert the list to a set
    unique_names = set(names) 
    print(f"unique names      = {unique_names}")

    # convert the unique names set to a list
    unique_names_list = list(unique_names)
    print(f"unique_names_list = {unique_names_list}")
    
# function6()

def function7():
    # empty list
    # empty_list = []
    empty_list = list()
    print(f"empty_list  = {empty_list}, type = {type(empty_list)}")

    # empty tuple
    # empty_tuple = ()
    empty_tuple = tuple()
    print(f"empty_tuple = {empty_tuple}, type = {type(empty_tuple)}")

    # this line will NOT create an empty set
    # instead it will create an empty dictionary
    # empty_set = {}
    # print(f"empty_set   = {empty_set}, type = {type(empty_set)}")

    # empty set
    empty_set = set()
    print(f"empty_set   = {empty_set}, type = {type(empty_set)}")


function7()

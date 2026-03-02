# list: mutable collection (can be updated at run time)
# tuple: immutable collection (once created, CAN NOT change)
# common properties
# - collection of similar or dissimilar values
# - allow duplicates
# - indexing (positive and negative)
# - slicing
# - ordered collection: the insertion order is maintained
# uncommon properties
# - list is mutable while tuple is immutable

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list  = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = 10, 20, 30, 40, 50
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")

# function1()

def function2():     
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list  = {numbers_list}, type = {type(numbers_list)}")

    # convert a list to a tuple
    numbers_tuple = tuple(numbers_list)
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")
    
# function2()


def function3():     
    # tuple of numbers
    numbers_tuple = 10, 20, 30, 40, 50
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")

    # convert a tuple into a list
    numbers_list = list(numbers_tuple)
    print(f"numbers_list  = {numbers_list}, type = {type(numbers_list)}")

function3()

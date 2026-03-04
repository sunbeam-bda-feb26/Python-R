import numpy as np

# indexing
# - reading values from array using index positions
# - types
#   - single value indexing
#     - reading single value using +ve or -ve index positions
#   - multi value indexing
#     - reading multiple values using multiple index positions
#     - returns a list of values

# slicing
# - same as list
# - please look at the example we have seen in list category 

def function1():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"numbers    = {numbers}")
    print('-' * 80)

    # single value indexing
    # using positive index position
    print(f"value at 0th index = {numbers[0]}")
    print(f"value at 1st index = {numbers[1]}")
    print(f"value at 2nd index = {numbers[2]}")
    print(f"value at 3rd index = {numbers[3]}")
    print(f"value at 4th index = {numbers[4]}")
    print('-' * 80)

    # using negative index position
    print(f"value at -1 index  = {numbers[-1]}")
    print(f"value at -2 index  = {numbers[-2]}")
    print(f"value at -3 index  = {numbers[-3]}")
    print(f"value at -4 index  = {numbers[-4]}")
    print(f"value at -5 index  = {numbers[-5]}")
    print('-' * 80)

# function1()
     
def function2():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"numbers                    = {numbers}")
    print('-' * 80)

    # multi-value indexing with positive index positions
    # reading values using multiple index positions at a time

    # [20, 30, 10, 50]
    print(f"numbers[[1, 2, 0, 4]]      = {numbers[[1, 2, 0, 4]]}")

    # [50, 90]
    print(f"numbers[[4, 8]]            = {numbers[[4, 8]]}")
    print('-' * 80)

    # multi-value indexing with negative index positions
    # reading values using multiple index positions at a time

    # [20, 30, 10, 50]
    print(f"numbers[[-9, -8, -10, -6]] = {numbers[[-9, -8, -10, -6]]}")

    # [50, 90]
    print(f"numbers[[-6, -2]]          = {numbers[[-6, -2]]}")
    print('-' * 80)

    # multi-value indexing with postive and negative index positions
    # reading values using multiple index positions at a time

    # [20, 30, 10, 50]
    print(f"numbers[[1, 2, -10, -6]]   = {numbers[[1, 2, -10, -6]]}")

    # [50, 90]
    print(f"numbers[[-6, 8]]           = {numbers[[-6, 8]]}")
    print('-' * 80)

# function2()

def function3():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers                  = {numbers}")

    # multi-value indexing with boolean index positions
    # reading values using multiple index positions at a time
    # - order of the elements is maintained

    # [30, 40]
    print(f"numbers[[F, F, T, T, F]] = {numbers[[False, False, True, True, False]]}")

    # [10, 30, 50]
    print(f"numbers[[T, F, T, F, T]] = {numbers[[True, False, True, False, True]]}")

# function3()



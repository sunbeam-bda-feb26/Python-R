# utility methods
# - index()
#   - used to return an index position of a value
#   - parameters
#     - value: value to be searched
#     - start_position: from where to start searching for the value, default is 0
# - count(): used to find the number of ocurrances of a value
# - sort(): used to sort the collection in ascending or descending order
# - reverse(): used to reverse the collection

def function1():
    # list of numbers
    numbers = [10, 9, 3, 6, 10, 4, 8, 9, 2, 6, 8, 10]
    print(f"numbers     = {numbers}")

    # find the index of value 2
    print(f"index of 2  = {numbers.index(2)}")

    # find the index of value 10
    print(f"index of 10 = {numbers.index(10)}")
    print(f"index of 10 = {numbers.index(10, 1)}")
    print(f"index of 10 = {numbers.index(10, 5)}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 9, 3, 6, 10, 4, 8, 9, 2, 6, 8, 10]
    print(f"numbers     = {numbers}")

    # find the number of ocurrances of 10
    print(f"value 10 is present {numbers.count(10)} times")
    print(f"value 9 is present  {numbers.count(9)} times")
    print(f"value 2 is present  {numbers.count(2)} times")

# function2()

def function3():
    # list of numbers
    numbers = [10, 9, 3, 10, 6, 10, 4, 8, 9, 2, 10, 6, 8, 10]
    print(f"numbers     = {numbers}")

    # find the index positions of 10

    # step1: find the count of value 10
    count = numbers.count(10)
    print(f"value 10 is present {count} times")

    # step2: find the index positions 
    start_position = 0

    # in python, if a variable is not required, but it has to be declared
    # for the syntax reason, use _ instead of a valid name
    for _ in range(count):
        index_position = numbers.index(10, start_position)
        print(f"value 10 is present at: {index_position}")

        # update the start_positions
        start_position = index_position + 1

# function3()

def function4():
    # list of numbers
    numbers = [10, 9, 3, 6, 10, 4, 8, 9, 2, 6, 8, 10]
    print(f"numbers = {numbers}")

    # sort the values in ascending order
    # numbers.sort()
    # print(f"numbers = {numbers}")

    # sort the values in descending order
    numbers.sort(reverse=True)
    print(f"numbers = {numbers}")

# function4()

def function5():
    # list of numbers
    numbers = [10, 9, 3, 6, 10, 4, 8, 9, 2, 6, 8, 10]
    print(f"numbers = {numbers}")

    # reverse the collection
    numbers.reverse()
    print(f"numbers = {numbers}")

# function5()

def function6():
    # list of numbers
    numbers = [10, 9, 3, 6, 10, 4, 8, 9, 2, 6, 8, 10]
    print(f"numbers     = {numbers}")

    # shallow copy
    # creating a new reference to the existing collection
    # if numbers or new_numbers get updated, other one will also reflect the same change
    # new_numbers = numbers

    # deep copy
    # create a copy of numbers list
    new_numbers = numbers.copy()
    print(f"new_numbers = {new_numbers}")

    # sort the numbers
    numbers.sort()
    print(f"numbers     = {numbers}")
    print(f"new_numbers = {new_numbers}")

# function6()


def function7():
    # list of numbers
    numbers = [10, 9, 3, 6, 10, 4, 8, 9, 2, 6, 8, 10]
    print(f"numbers = {numbers}")

    # update value at 2nd index to 500
    numbers[2] = 500
    print(f"numbers = {numbers}")

function7()

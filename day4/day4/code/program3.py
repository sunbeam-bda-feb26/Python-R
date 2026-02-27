# List methods
# - pop()
#   - by default, used to remove the last value
#   - returns the value removed from the collection
#   - if no parameter is passed, the last value will be removed
#   - if an index is passed, the value at the specified index will be removed
# - remove()
#   - used to remove a value by value not by index
#   - does not return anything
# - clear()
#   - used to remove all values from the collection
#   - does not return anything

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # remove the last value from the collection
    removed_value = numbers.pop()
    print(f"numbers = {numbers}, length = {len(numbers)}, removed value = {removed_value}")

    # remove the last value from the collection
    removed_value = numbers.pop()
    print(f"numbers = {numbers}, length = {len(numbers)}, removed value = {removed_value}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers   = {numbers}, length = {len(numbers)}")

    # remove a value at 1st index
    removed_value = numbers.pop(1)
    print(f"numbers   = {numbers}, length = {len(numbers)}, removed value = {removed_value}")
    print('-' * 80)

    # list of countries
    countries = ["india", "usa", "uk", "china", "japan"]
    print(f"countries = {countries}")

    # remove china from the collection
    # countries.pop(3)
    countries.pop(countries.index('china'))
    print(f"countries = {countries}")
    print('-' * 80)

    # remove a value from invalid index
    # will raise an exception: IndexError: pop index out of range
    # countries.pop(100)
    # print(f"countries = {countries}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers   = {numbers}, length = {len(numbers)}")

    # remove value 20
    # here 20 is not the index, but it is the value to be removed
    numbers.remove(20)
    print(f"numbers   = {numbers}, length = {len(numbers)}")

    # remove a invalid value from collection
    # will raise an exception: ValueError: list.remove(x): x not in list
    numbers.remove(100)
    print(f"numbers = {numbers}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers   = {numbers}, length = {len(numbers)}")

    # remove all the values from collection
    numbers.clear()
    print(f"numbers   = {numbers}, length = {len(numbers)}")

# function4()

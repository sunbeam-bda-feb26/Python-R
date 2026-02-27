# List
# - ordered mutable collection of similar or dissimilar values
# - allows duplicate values
# - mutable collection
#   - can add new value at run time
#   - update existing values at run time
#   - remove existing values at run time
#   - reverse the collection
# - range()
#   - used to create a collection with sequential values
#   - parameters
#     - start: 
#       - start value to create the collection
#       - default value = 0
#     - stop: 
#       - last value to stop the collection at
#       - stop value is excluded from the generated values
#     - step: 
#       - get the next value to add in the collection
#       - default value = 1
# - methods
#   - append(): used to append only one value at the end of the list
#   - extend(): used to append multiple values at the end of the list
#   - insert(): used to insert only one value anywhere inside the list
#   - index(): used to get an index of a value

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, type = {type(numbers)}")

    # iterate over the list
    for number in numbers:
        print(f"number = {number}, number^2 = {number ** 2}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # add value at the end of the list
    numbers.append(60)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # add value at the end of the list
    numbers.append(60)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # add value at the end of the list
    numbers.append(60)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # append value 70 at the end of the list
    numbers.append(70)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # append values 80, 90 and 100 at the end of the list
    numbers.extend([80, 90, 100])
    print(f"numbers = {numbers}, length = {len(numbers)}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # insert a value 15 between 10 and 20
    numbers.insert(1, 15)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # insert a value 25 between 20 and 30
    numbers.insert(3, 25)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # insert a value 35 between 30 and 40
    numbers.insert(5, 35)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # insert a value 45 between 40 and 50
    numbers.insert(7, 45)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # insert a value 5 on the 0th index
    numbers.insert(0, 5)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # insert a value 75 at 15th position
    numbers.insert(15, 75)
    print(f"numbers = {numbers}, length = {len(numbers)}")

    # print(f"value at 15th position = {numbers[15]}")

# function3()

def function4():
    # list of strings
    countries = ["india", "usa", "uk", "japan"]
    print(f"countries = {countries}")
    print('-' * 80)

    # insert value 'bhutan' at the 'uk's position

    # find the index of 'uk'
    index = 0
    for country in countries:
        if country == 'uk':
            break
        index += 1
    
    # insert the value 'bhutan' at the indexth position
    countries.insert(index, 'bhutan')
    print(f"countries = {countries}")

# function4()

def function5():
    # list of strings
    countries = ["india", "usa", "uk", "japan"]
    print(f"countries = {countries}")
    print('-' * 80)

    # insert value 'bhutan' at the 'uk's position
    index_of_uk = countries.index("uk")
    print(f"index of uk = {index_of_uk}")

    # insert the value 'bhutan' at the indexth position
    countries.insert(index_of_uk, 'bhutan')
    print(f"countries = {countries}")

# function5()

def function6():
    # create a collection of 1 to 10 values
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = list(range(1, 11))
    print(f"numbers          = {numbers}")
    print(f'-' * 80)

    # step = 1
    print(f"range(1, 11)     = {list(range(1, 11))}")
    print(f"range(1, 11, 1)  = {list(range(1, 11, 1))}")
    print(f"range(1, 11, 2)  = {list(range(1, 11, 2))}")
    print(f"range(1, 11, 3)  = {list(range(1, 11, 3))}")
    print(f'-' * 80)

    # start = 0, step = 1
    print(f"range(11)        = {list(range(11))}")
    print(f'-' * 80)

    # if step value is negative, start and stop will be swapped
    print(f"range(11, 1, -1) = {list(range(11, 1, -1))}")
    print(f'-' * 80)

    for number in range(5):
        print(f"number = {number}")

    print(f'-' * 80)

    # list of numbers
    numbers = [10, 20, 30, 40, 50]

    # iterate over numbers using traditional style (using index to get the value)
    for index in range(len(numbers)):
        print(f"value at index {index} = {numbers[index]}")

function6()

def function7():
    # create a collection of person names
    names = []

    # get the number of persons from user
    count = int(input("enter no of persons information to collect: "))

    # run the for loop for count number of times
    for index in range(count):
        
        # get person name from user
        name = input(f"enter person {index} name: ")

        # append the name to the names collection
        names.append(name)

    # print all the names collected
    print(f"names = {names}")

# function7()


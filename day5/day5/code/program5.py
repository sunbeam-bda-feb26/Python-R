# multi-dimensional collection
# - collection of collections
# - e.g. list of lists, list of tuples, tuple of tuples, 
#   tuple of lists, list of dictionaries
# - a row can have any no of columns

def function1():
    # list of numbers (1D collection)
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers[0]    = {numbers[0]}")
    print(f"numbers[1]    = {numbers[1]}")
    print(f"numbers[2]    = {numbers[2]}")
    print(f"-" * 80)

    # list of lists (2D collection)
    # multidimensional collection with 3 rows and 2 columns each
    numbers = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    print(f"numbers[0]    = {numbers[0]}")
    print(f"numbers[1]    = {numbers[1]}")
    print(f"numbers[2]    = {numbers[2]}")
    print(f"-" * 80)

    # read first row
    print(f"numbers[0][0] = {numbers[0][0]}")
    print(f"numbers[0][1] = {numbers[0][1]}")

    # read second row
    print(f"numbers[1][0] = {numbers[1][0]}")
    print(f"numbers[1][1] = {numbers[1][1]}")

    # read third row
    print(f"numbers[2][0] = {numbers[2][0]}")
    print(f"numbers[2][1] = {numbers[2][1]}")
    
# function1() 

def function2():
    # 2D collection
    # every row has different columns
    numbers = [
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90]
    ]
    print(f"numbers[0]    = {numbers[0]}")
    print(f"numbers[1]    = {numbers[1]}")
    print(f"numbers[2]    = {numbers[2]}")
    print(f"-" * 80)

    # add a new row
    numbers.append([100, 110, 120, 130, 140])

    # add a new column in first row
    numbers[0].append(30)

    # iterate over the rows
    for row in numbers:
        print(f"row        = {row}")

        # iterate over the columns
        for column in row:
            print(f"column     = {column}")

        print('-' * 80)

# function2()

def function3():
    # 2D collection
    # list of tuples
    numbers = [
        (10, 20),
        (30, 40, 50),
        (60, 70, 80, 90)
    ]
    print(f"type of nubers = {type(numbers)}")
    print(f"numbers[0]     = {numbers[0]}")
    print(f"numbers[1]     = {numbers[1]}")
    print(f"numbers[2]     = {numbers[2]}")
    print(f"-" * 80)

    # add a new row
    numbers.append((100, 110, 120, 130, 140))

    # add a new column in first row
    # this is not possible as the inner collection is tuple
    # tuple is immutable
    # numbers[0].append(30)

    # iterate over the rows
    for row in numbers:
        print(f"row         = {row}")

        # iterate over the columns
        for column in row:
            print(f"column      = {column}")

        print('-' * 80)

# function3()

def function4():
    # 2D collection
    # tuple of tuples
    numbers = (
        (10, 20),
        (30, 40, 50),
        (60, 70, 80, 90)
    )
    print(f"type of numbers = {type(numbers)}")

    # add a new row
    # NOT possible as tuple is immutable
    # numbers.append((100, 110, 120, 130, 140))

    # add a new column in first row
    # NOT possible as tuple is immutable
    # numbers[0].append(30)

    # iterate over the rows
    for row in numbers:
        print(f"row           = {row}")

        # iterate over the columns
        for column in row:
            print(f"column        = {column}")

        print('-' * 80)

# function4()

def function5():
    # 2D collection
    # tuple of lists
    numbers = (
        [10, 20],
        [30, 40, 50],
        [60, 70, 80, 90]
    )
    print(f"type of numbers = {type(numbers)}")

    # add a new row
    # NOT possible as tuple is immutable
    # numbers.append((100, 110, 120, 130, 140))

    # add a new column in first row
    numbers[0].append(30)

    # iterate over the rows
    for row in numbers:
        print(f"row           = {row}")

        # iterate over the columns
        for column in row:
            print(f"column        = {column}")

        print('-' * 80)

# function5()

def function6():
    # list of dictionaries
    persons = [
        {"name": "john", "email": "john@test.com", "age": 30, "phone": "+91243232"},
        {"name": "jane", "email": "jane@test.com", "age": 10, "address": "pune"},
        {"name": "linda", "email": "linda@test.com", "age": 90, "company": "sunbeam"}
    ]
    
    # get individual persons
    print(f"persons[0]       = {persons[0]}")
    print(f"persons[1]       = {persons[1]}")
    print(f"persons[2]       = {persons[2]}")
    print('-' * 80)

    # iterate over the persons and get the person info
    for person in persons:
        # print(f"person = {person}")

        # iterate over the dictionary and get all the info
        for key, value in person.items():
            print(f"{key} = {value}")
        print('-' * 80)


function6()
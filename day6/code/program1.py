# higher oder functions
# - functions which accept another function as a parameter

# map: used for transformation
# filter: used for selection
# combination of map and filter
# - most often filter() is used before the map()

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # function to transform a value to its cube
    cube = lambda n: n ** 3

    # cube of every single number
    cubes = list(map(cube, numbers))
    print(f"cubes   = {cubes}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 30, 48, 27, 71, 92, 94, 47]
    print(f"numbers     = {numbers}")

    # selection function: function to select only odd numbers
    is_odd = lambda n: n % 2 != 0

    # find odd numbers
    odd_numbers = list(filter(is_odd, numbers))
    print(f"odd numbers = {odd_numbers}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 30, 48, 27, 71, 92, 94, 47]
    print(f"numbers                = {numbers}")

    # square of even numbers
    # step1: find the even numbers
    is_even = lambda n: n % 2 == 0
    even_numbers = list(filter(is_even, numbers))
    print(f"even numbers           = {even_numbers}")

    # step2: get the square of even numbers
    square = lambda n: n ** 2
    square_even_numbers = list(map(square, even_numbers))
    print(f"square of even numbers = {square_even_numbers}")

# function3()

def function4():
    # list of dictionaries
    persons = [
        {"name": "person1", "age": 10, "address": "pune"},
        {"name": "person2", "age": 40, "address": "mumbai"},
        {"name": "person3", "age": 68, "address": "pune"},
        {"name": "person4", "age": 13, "address": "chennai"},
        {"name": "person5", "age": 47, "address": "satara"},
        {"name": "person6", "age": 29, "address": "pune"}
    ]
    print(f"persons = {persons}")
    print(f'-' * 80)

    # get all person names from the collection
    get_name = lambda person: person['name']
    names = list(map(get_name, persons))
    print(f"all person names = {names}")
    print(f'-' * 80)

    # find the persons eligible for voting
    is_eligible = lambda person: person['age'] >= 18
    eligible_persons = list(filter(is_eligible, persons))
    print(f"eligible persons = {eligible_persons}")
    print('-' * 80)

    # find the name of all the persons from 'pune'
    is_person_from_pune = lambda person: person['address'] == 'pune'
    persons_from_pune = list(filter(is_person_from_pune, persons))
    names_from_pune = list(map(get_name, persons_from_pune))
    print(f"names from pune  = { names_from_pune}")

function4()


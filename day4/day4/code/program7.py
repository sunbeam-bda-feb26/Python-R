# tuple
# - immutable ordered collection of similar or dissimilar values
# - immutable collection is preferred over mutable collection
# - methods not supported: append, extend, pop, insert, remove, clear, sort, reverse
# - supported methods: index(), count()

# tuple packing
# - multiple values get packed into tuple 
# - e.g. numbers = 10, 20, 30, 40
#   - numbers will be created as a tuple with 10, 20, 30, 40 values

# tuple unpacking
# - creating individual variables with values at specific index positions
#   - e.g. numbers = (10, 20)
#   - n1, n2 = numbers
#     - n1 = numbers[0], n2 = numbers[1]

# packing and unpacking
# - n1, n2 = 10, 20

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list   = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = (10, 20, 30, 40, 50)
    print(f"numbers_tuple  = {numbers_tuple}, type = {type(numbers_tuple)}")

    # tuple of numbers created using tuple packing
    numbers_tuple = 10, 20, 30, 40, 50
    print(f"numbers_tuple  = {numbers_tuple}, type = {type(numbers_tuple)}")

# function1()

def function2():
    # list with single value
    numbers_list = [10]
    print(f"numbers_list   = {numbers_list}, type = {type(numbers_list)}")

    # this is NOT a tuple with a single value
    # rather it will be treated as an int variable
    # numbers_tuple = (10)
    
    # tuple with a single value
    # numbers_tuple = 10,
    numbers_tuple = (10, )
    print(f"numbers_tuple  = {numbers_tuple}, type = {type(numbers_tuple)}")

    # tuple with one value
    # names_tuple = "john",
    names_tuple = ("john", )
    print(f"names_tuple  = {names_tuple}, type = {type(names_tuple)}")

# function2()

def function3():
    # tuple of numbers
    numbers = 10, 20, 30
    print(f"numbers = {numbers}, type = {type(numbers)}")
    print(f"-" * 80)

    # read values from tuple and store them in individual variables
    # n1 = numbers[0]
    # n2 = numbers[1]
    # n3 = numbers[2]

    # tuple unpacking
    # - read values from tuple and store them in individual variables
    n1, n2, n3 = numbers

    print(f"n1 = {n1}, type = {type(n1)}")
    print(f"n2 = {n2}, type = {type(n2)}")
    print(f"n3 = {n3}, type = {type(n3)}")

# function3()

def function4():
    n1 = 10
    n2 = 20
    print(f"n1 = {n1}, n2 = {n2}")

    # swapping values
    # - first a tuple packing will create a tuple with (20, 10) values
    # - the same tuple will be broken into n1 and n2 with 0 and 1 position
    n1, n2 = n2, n1
    print(f"n1 = {n1}, n2 = {n2}")

    # temp = n1
    # n1 = n2
    # n2 = temp
    # print(f"n1 = {n1}, n2 = {n2}")

# function4()

def function5():
    # tuple with numbers
    numbers = 10, 20, 30, 40, 50
    print(f"numbers = {numbers}, type = {type(numbers)}")
    print('-' * 80)

    # unpack the tuple
    n1, n2, n3, n4, n5 = numbers
    print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}, n4 = {n4}, n5 = {n5}")
    print('-' * 80)

    # unpack the tuple with more values into less variables
    # will raise an error - ValueError: too many values to unpack (expected 2)
    # a1, a2 = numbers

    # unpack the tuple
    # a1 = numbers[0] = 10
    # a2 = numbers[1] = 20
    # a3 = rest of the values = [30, 40, 50]
    a1, a2, *a3 = numbers
    print(f"a1 = {a1}, a2 = {a2}, a3 = {a3}")
    print('-' * 80)

    b1, *b2, b3 = numbers
    print(f"b1 = {b1}, b2 = {b2}, b3 = {b3}")
    print('-' * 80)

    *c1, c2, c3 = numbers
    print(f"c1 = {c1}, c2 = {c2}, c3 = {c3}")
    print('-' * 80)

    # more than one * is not allowed while unpacking the tuple
    # *d1, d2, *d3 = numbers
    # print(f"d1 = {d1}, d2 = {d2}, d3 = {d3}")
    # print('-' * 80)

# function5()

def function6():
    # tuple of numbers
    numbers = 10, 20, 30, 40, 50
    print(f"nubers = {numbers}")

    # append a value to the end of the tuple
    # numbers.append(60)
    # print(f"nubers = {numbers}")

function6()

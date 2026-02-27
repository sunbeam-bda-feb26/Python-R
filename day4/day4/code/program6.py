# slicing
# - retrieving the values from sequential index positions
# - collection[start:stop:step]
# - always returns a new collection

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers = {numbers}")
    print('-' * 80)

    # [30, 40, 50, 60, 70]
    values = []
    for index in range(2, 7):
        values.append(numbers[index])

    print(f"slice   = {values}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers         = {numbers}")
    print('-' * 80)

    # [30, 40, 50, 60, 70]
    print(f"numbers[2:7]    = {numbers[2:7]}")

    # [60, 70]
    print(f"numbers[5:7]    = {numbers[5:7]}")

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[0:11]   = {numbers[0:11]}")

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[0:11:1] = {numbers[0:11:1]}")

    # [10, 30, 50, 70, 90]
    print(f"numbers[0:11:2] = {numbers[0:11:2]}")

    # [20, 40, 60, 80, 100]
    print(f"numbers[1:11:2] = {numbers[1:11:2]}")

# function2()

def function3():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers         = {numbers}")
    print('-' * 80)

    # [10, 20, 30, 40, 50]
    print(f"numbers[0:5]    = {numbers[0:5]}")

    # [10, 20, 30, 40, 50]
    # start has a default value of 0
    print(f"numbers[:5]     = {numbers[:5]}")

    # [10, 20, 30, 40, 50]
    # start has a default value of 0
    print(f"numbers[:5:1]   = {numbers[:5:1]}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers         = {numbers}")
    print('-' * 80)

    # [60, 70, 80, 90, 100]
    print(f"numbers[5:11]   = {numbers[5:11]}")

    # [60, 70, 80, 90, 100]
    # stop has a default value of last position of the collection
    print(f"numbers[5:]     = {numbers[5:]}")

    # [60, 70, 80, 90, 100]
    # stop has a default value of last position of the collection
    print(f"numbers[5::1]   = {numbers[5::1]}")

# function4()


def function5():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers         = {numbers}")
    print('-' * 80)

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[0:11:1] = {numbers[0:11:1]}")

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[0:11]   = {numbers[0:11]}")

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[0:]     = {numbers[0:]}")

    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[:]      = {numbers[:]}")
    
    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[::]     = {numbers[::]}")

# function5()

def function6():
    # list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers           = {numbers}")
    print('-' * 80)

    # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(f"numbers[12:0:-1]  = {numbers[12:0:-1]}")

    # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(f"numbers[11::-1]   = {numbers[11::-1]}")

    # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(f"numbers[::-1]     = {numbers[::-1]}")

    # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    # returns empty list since its a invalid combination of start and stop
    # start and stop must be of same kind (either +ve or -ve)
    # print(f"numbers[-1:5:1]   = {numbers[-1:5:1]}")

# function6()

def function7():
    # string
    name = "sunbeam"

    print(f"name          = {name}")
    print(f"reversed name = {name[::-1]}")
    print(f"name[3:]      = {name[3:]}")
    print(f"name[:3]      = {name[:3]}")

# function7()
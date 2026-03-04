import numpy as np

# multi-dimensional array
# - it is mandatory to have same no of columns in every row
# - it gets created as a flat memory

# reshape
# - instead of allocating new memory, read existing memory with different strategy
# - data will NOT be copied

def print_array_properties(numbers):
    print(f"numbers                 = {numbers}")
    print(f"type                    = {type(numbers)}")

    # get the data type of every value in the array
    print(f"data type of every item = {numbers.dtype}")

    # get the size of every item
    print(f"size of every time      = {numbers.itemsize} bytes")

    # get the length of array
    print(f"length of array         = {numbers.size}")

    # get total memory required to store this array
    print(f"total bytes required    = {numbers.itemsize * numbers.size} bytes")
    print(f"total bytes required    = {numbers.nbytes} bytes")

    # get the number of dimensions
    print(f"no of dimensions        = {numbers.ndim}")

    # get the shape of array
    print(f"shape of array          = {numbers.shape}")
    print(f'-' * 80)

    # get the flags of array
    print(numbers.flags)

def function1():
    # 2d array 
    array = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print_array_properties(array)

    # 3d array
    array = np.array([
        [
            [10, 20, 10],
            [30, 40, 30]
        ],
        [
            [50, 60, 50],
            [70, 80, 70]
        ]
    ])
    print_array_properties(array)

# function1()

def function2():
    # 1d array
    numbers = np.array([10, 20, 30, 40, 50, 60])
    print_array_properties(numbers)

    # 2d array with 2x3 
    numbers2 = numbers.reshape([2, 3])
    print_array_properties(numbers2)

    # 2d array with 3x2
    numbers2 = numbers.reshape([3, 2])
    print_array_properties(numbers2)

    # 2d array with 1x6
    numbers2 = numbers.reshape([1, 6])
    print_array_properties(numbers2)

    # 2d array with 6x1
    numbers2 = numbers.reshape([6, 1])
    print_array_properties(numbers2)

# function2()

def function2():
    # 2d array 
    array = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print_array_properties(array)

    for row in array:
        print(f"row = {row}")
        for col in row:
            print(f"col = {col}")

# function2()




# numpy
# - stands for numeric python
# - used to store the huge data in the form of ndarray (n dimensional array)
# - memory and space efficient
# - third party package
# - needs to be installed using any package manager
# - developed in C
# - install numpy using pip
#   - pip install numpy

# ndarray
# - n dimensional array
# - immutable collection of similar values
# - all values in the array will be stored continguously
# - reading the values from array is faster than list

# package manager
# - program used to manage (install/uninstall/upgrade) the external packages
# - e.g.
#   - pip: system package manager (defualt)
#   - conda: external package manager
#   - uv: faster alternative to pip
#   - poetry: alternative to pip
# using pip
# - windows: pip
# - macOS / linux: pip3
# - operations
#   - install a package: pip install <package name>
#   - uninstall a package: pip uninstall <package name>
#   - find the details of a package: pip show <package name>
#   - upgrade the package: pip upgrade <package name>

# numpy data types
# - int  : int8, int16, int32, int64
# - float: float16, float32, float64
# - boolean
# - str (object)

# import numpy package
import numpy as np

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list  = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = 10, 20, 30, 40, 50
    print(f"numbers_tuple = {numbers_tuple}, type = {type(numbers_tuple)}")

    # array of numbers
    numbers_array = np.array([10, 20, 30, 40, 50])
    print(f"numbers_array = {numbers_array}, type = {type(numbers_array)}")

# function1()

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
    # print(numbers.flags)

def function2():
    # array of numbers where every item is int64 
    numbers = np.array([10, 20, 30, 40, 50, 60])
    print_array_properties(numbers)
    
    # array of numbers where every item is int32
    numbers = np.array([10, 20, 30, 40, 50, 60], dtype=np.int32)
    print_array_properties(numbers)

    # array of numbers where every item is int16
    numbers = np.array([10, 20, 30, 40, 50, 60], dtype=np.int16)
    print_array_properties(numbers)

    # array of numbers where every item is int8
    numbers = np.array([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print_array_properties(numbers)
    
# function2()

def function3():
    # array of numbers where every item is int8 
    numbers = np.array([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print_array_properties(numbers)

    # read the values from array
    # calculate the address of the item to read the value
    # assume the array is stored at (base_address) = 0x15000

    # item address     = base_address + (position * item_size)
    # 0th item address = 0x15000 + (0 * 8) = 0x15000
    print(f"value at 0th index = {numbers[0]}")

    # 1st item address = 0x15000 + (1 * 8) = 0x15008
    print(f"value at 1st index = {numbers[1]}")
    print(f"value at 2nd index = {numbers[2]}")
    print(f"value at 3rd index = {numbers[3]}")
    print(f"value at 4th index = {numbers[4]}")

    # 5th item address = 0x15000 + (5 * 8) = 0x15040
    print(f"value at 5th index = {numbers[5]}")

# function3()

def function4():
    # list of integers
    numbers = np.array([10, 20, 30, 40, 50])
    print_array_properties(numbers)

    # list of floats
    numbers = np.array([10.5, 20.5, 30.5, 40.5, 50.5])
    print_array_properties(numbers)

    # list of strings
    countries = np.array(['india', 'usa', 'uk', 'japan', 'sri lanka'])
    print_array_properties(countries)

# function4()

def function5():
    # create a float array with all zeros
    zeros = np.zeros(5)
    print(f"zeros   = {zeros}")

    # create an int array with all zeros
    zeros = np.zeros(5, dtype=np.int8)
    print(f"zeros   = {zeros}")

    # create a float array with all ones
    ones = np.ones(5)
    print(f"ones    = {ones}")

    # create an int array with all ones
    ones = np.ones(5, dtype=np.int8)
    print(f"ones    = {ones}")

    # create an array using range
    array = np.arange(10)
    print(f"array   = {array}")

    # create an array with random numbers
    # low : lowest value
    # high: highest value
    # size: no of values required
    array = np.random.randint(10, 50, 10)
    print(f"array   = {array}")

# function5()

def function6():
    # array of numbers
    numbers = np.array([10, 20, 30, 40, 50])
    print(f"numbers = {numbers}")

    # change the value at 3rd position
    numbers[3] = 40000
    print(f"numbers = {numbers}")

function6()

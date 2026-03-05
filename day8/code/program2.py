# pandas
# - used for data engineering (data loading, analysis and analytics)
# - developed on top of numpy
# - data structures
#   - series
#   - data frame
#   - panel

# series
# - one dimensional array 
# - used numpy array behind scene
# - series stores the values using different array named `values`
# - series stores the index positions using different array named `index`
# - series supports only those index positions, 
#   which are present in the index collection
# - indexing in series will always return a new value (unique index) 
#   or series (if index is present multiple times)

import numpy as np
import pandas as pd

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50]
    print(f"numbers_list           = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = 10, 20, 30, 40, 50
    print(f"numbers_tuple          = {numbers_tuple}, type = {type(numbers_tuple)}")

    # array of numbers
    numbers_array = np.array([10, 20, 30, 40, 50])
    print(f"numbers_array          = {numbers_array}, type = {type(numbers_array)}")

    # series of numbers
    numbers_series = pd.Series([10, 20, 30, 40, 50])
    print(f"type of numbers_series = {type(numbers_series)}")
    print(numbers_series)

# function1()

def function2():
    # series of numbers
    numbers = pd.Series([10, 20, 30, 40, 50])

    print(f"length of series      = {numbers.size}")
    print(f"shape of series       = {numbers.shape}")
    print(f"dimension of series   = {numbers.ndim}")
    print(f"data type             = {numbers.dtype}")
    print(f"no of bytes           = {numbers.nbytes} bytes")

    # itemsize is not support
    # print(f"item size             = {numbers.itemsize} bytes")
    print(f"item size             = {numbers.nbytes // numbers.size} bytes")    

    print(f"index positions       = {numbers.index}")
    print(f"values                = {numbers.values}")

# function2()

def function3():
    # series of numbers
    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)
    print('-' * 80)

    # single value indexing with positive values
    print(f"numbers[0]  = {numbers[0]}")
    print(f"numbers[1]  = {numbers[1]}")
    print(f"numbers[2]  = {numbers[2]}")
    print(f"numbers[3]  = {numbers[3]}")
    print(f"numbers[4]  = {numbers[4]}")

    # single value indexing with negative values
    # since the -1 is not present in the index positions, 
    # this line will raise an exception
    # print(f"numbers[-1] = {numbers[-1]}")

# function3()
    
def function4():
    # series of numbers
    numbers = pd.Series(
        # values
        [10, 20, 30, 40, 50],

        # index positions
        index=[-1, -2, -3, -4, -5]
    )
    
    print(numbers)
    print('-' * 80)

    print(f"numbers.index  = {numbers.index}")
    print(f"numbers.values = {numbers.values}")
    print('-' * 80)

    # single value indexing with positive values
    # since the 0 is not present in the index positions, 
    # this line will raise an exception
    # print(f"numbers[0]   = {numbers[0]}")

    # single value indexing with negative values
    print(f"numbers[-1]    = {numbers[-1]}")
    print(f"numbers[-2]    = {numbers[-2]}")
    print(f"numbers[-3]    = {numbers[-3]}")
    print(f"numbers[-4]    = {numbers[-4]}")
    print(f"numbers[-5]    = {numbers[-5]}")

# function4()

def function5():
    # series of string values
    # since the index is not provides, 
    # the indexes will be generated automatically (sequentially from 0 to len - 1)
    models = pd.Series(["i10", "triber", "X5", "Meredian"])
    print(models)
    print('-' * 80)

    models = pd.Series(
        # values
        ["i10", "triber", "X5", "Meredian", "i20", "compass"],

        # index
        index=["hyundai", "renault", "bmw", "jeep", "hyundai", "jeep"]
    )

    print(models)
    print('-' * 80)
    print(f"index            = {models.index}")
    print(f"values           = {models.values}")

    # what is the model of bmw
    print(f"model of bmw     = {models['bmw']}")
    print(f"model of hyundai = {models['hyundai']}")
    print(f"model of jeep    = {models['jeep']}")

# function5()

def function6():
    # series of companies
    companies = pd.Series(
        # values
        ["hyundai", "renault", "bmw", "jeep", "hyundai", "jeep"],

        # index
        index=["i10", "triber", "X5", "Meredian", "i20", "compass"]
    )
    print(companies)
    print('-' * 80)
    print(f"index            = {companies.index}")
    print(f"values           = {companies.values}")

    print('-' * 80)
    print(f"company of i10   = {companies['i10']}")

    # since gls is not valid index, this line will raise an exception
    # print(f"company of gls   = {companies['gls']}")

# function6()
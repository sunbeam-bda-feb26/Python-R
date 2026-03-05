import numpy as np

def function1():
    # 2d array
    array = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    # get the data using [][]
    print(f"value at [0][0] = {array[0][0]}")
    print(f"value at [0][1] = {array[0][1]}")
    print(f"value at [0][2] = {array[0][2]}")

    # get the data using [,]
    print(f"value at [1, 0] = {array[1, 0]}")
    print(f"value at [1, 1] = {array[1, 1]}")
    print(f"value at [1, 2] = {array[1, 2]}")

# function1()

def function2():
    # array of numbers
    numbers1 = np.array([1, 2, 3, 4, 5])
    numbers2 = np.array([6, 7, 8, 9, 10])

    # broadcast addition operation with an array and a number
    # result[i] = numbers1[i] + 10
    print(f"numbers1 + 10       = {numbers1 + 10}")

    # broadcast addition operation with two arrays
    # the two arrays must be of same shape
    # result[i] = numbers1[i] + numbers2[i]
    print(f"numbers1 + numbers2 = {numbers1 + numbers2}")
    print(f"numbers1 - numbers2 = {numbers1 - numbers2}")
    print(f"numbers1 * numbers2 = {numbers1 * numbers2}")
    print(f"numbers1 / numbers2 = {numbers1 / numbers2}")

function2()

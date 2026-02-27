# indexing
# - accessing a single value using index position
# - types
#   - positive: index will start from 0 to len(collection) - 1
#   - negative: 
#     - index will start from -len(collection) to -1
#     - at the time of compilation, the negative index gets converted 
#       into positive one by adding it to the len(collection)
#     - e.g -3 => 5 - 3 = 2

def function1():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    print('-' * 80)

    # positive indexing
    # - starts from 0 to len(numbers) - 1
    print(f"numbers[0] = {numbers[0]}")
    print(f"numbers[1] = {numbers[1]}")
    print(f"numbers[2] = {numbers[2]}")
    print(f"numbers[3] = {numbers[3]}")
    print(f"numbers[4] = {numbers[4]}")

# function1()

def function2():
    # list of numbers
    numbers = [10, 20, 30, 40, 50]
    print(f"numbers = {numbers}")
    print('-' * 80)

    # negative indexing
    # - starts at -len(numbers) to -1
    # - -1 will be the last position
    print(f"numbers[-5] = {numbers[-5]}")
    print(f"numbers[-4] = {numbers[-4]}")
    print(f"numbers[-3] = {numbers[-3]}")
    print(f"numbers[-2] = {numbers[-2]}")
    print(f"numbers[-1] = {numbers[-1]}")

# function2()

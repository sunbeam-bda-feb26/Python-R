# a function can be passed as an argument to another function

# add here is a variable of type function
def add(p1: int, p2: int):
    return p1 + p2

# print(f"add = {add}, type = {type(add)}")

def subtract(p1: int, p2: int):
    return p1 - p2


# lambda function for multiplication
multiply = lambda p1, p2: p1 * p2

def execute(function):
    # function = multiply
    print(f"inside execute")
    print(f"function = {function}, type = {type(function)}")

    # call the function
    print(f"10 x 30 = {function(10, 30)}")

# execute(10)
# execute(15.50)
# execute("test")

# num = 200
# execute(num)

# calling execute function by passing add as a function
execute(add)
execute(subtract)
execute(multiply)
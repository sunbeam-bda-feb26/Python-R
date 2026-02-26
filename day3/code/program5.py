# functional programming language
# - function is considered as a first class citizen
#   - function is declared as a variable of type function
# - function can be passed to another function as a parameter
# - function can be returned as a return value of a function
# - e.g. map, filter, reduce

# rules for lambda
# - similar to inline function in "C"
# - lambda without a parameter is useless
# - lambda can accept 1 or more parameters
# - type hinting is NOT supported
# - lambda can NOT have more than 1 statement in its body
# - the lambda contains an expression which will be evaluated
#   before returning the value
# - return keyword is not required while returning value from lambda
#   - return keyword is by default assumed 

# declare a variable
num = 200
# print(f"num = {num}, type = {type(num)}")

# declare a function
def function1():
    print("inside function1")
    # my_var = 200

    def inner_function1():
        print(f"inside inner_function1")

    print(f"inner_function1 = {inner_function1}, type = {type(inner_function1)}")

# function1 is a reference pointing to an object of type function
# print(f"function1 = {function1}, type = {type(function1)}")

# function call
# function1()

# named function to get square of a number
# def square(number: int):
#     return number ** 2

# lambda function to get square of a number
square = lambda number: number ** 2
# print(f"square of 15 = {square(15)}")
# print(f"square = {square}, type = {type(square)}")

# get cube of a number using lambda
cube = lambda n: n ** 3
# print(f"cube of 7 = {cube(7)}")
# print(f"cube = {cube}, type = {type(cube)}")

# lambda function to add two numbers
add = lambda n1, n2 : n1 + n2
addition = add(20, 40)
print(f"20 + 40 = {addition}")
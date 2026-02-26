# function definition
# - function declaration: function name and list of parameters
# - function body: statements or block which will define the logic
# - function declaration and body can NOT be separated
# - types
#   - based on parameters
#     - parameterless: does not accept any parameter
#     - parameterized: accepts at least one parameter
# - function definition does not get called automatically
# - function requires a call to execute the function body
# - (global) function can be called anywhere in the code 
# - function can NOT be called before its definition
# - if return keyword is missing, function by default returns a None object
# - a function can return a value of ANY data type
# - if a value is returned by a function, it is optional to capture the returned result
# - calling convention
#   - how the parameters of a function will get the values assigned
#   - python uses Pascal calling convention
#   - the parameters will get assigned from left to right


# parameterless function definition
def function1():
    """
    This is dummy function.
    This is a parameterless function which returns None.
    """
    print("inside function1")
    print("another statement inside function1")

# __doc__: dunder doc
# print(function1.__doc__)
# print(print.__doc__)

# function call 
# function invocation
# function1()


# parameterized function definition
def function2(param: int):
    print("inside function2")
    print(f"param = {param}, type = {type(param)}")

# function call
# function2(100)
# function2("test")
# function2(None)

# parameter is mandatory
# - if missed, it raisess an error: TypeError
# function2()

# can not pass more no of parameter than expected
# function2(None, None)

def function3(p1: int, p2: int, p3: int):
    print("inside function3")
    # get the sum of all the parameters
    result = p1 + p2 + p3
    print(f"result = {result}")

# function3_return_value = function3(10, 20, 30)
# print(f"function3_return_value = {function3_return_value}")


def add(p1: int, p2: int):
    print('inside add function')
    # returning an expression
    # the express p1 + p2 will be resolved first
    # and the resul will be returned as a return value of add function
    return p1 + p2

    # all statements after return will NEVER get executed
    # as the return keyword by default exits the function execution
    # and the execution control will be passed to its caller
    # print("this is a statement after return keyword")

# call function add and capture its return value in add_result variable
# add_result = add(10, 20)
# print(f"add_result = {add_result}")

# call the function but do not capture the returned value
# add(20, 40)

# n1 = int(input("enter number1: "))
# n2 = int(input("enter number2: "))
# result = add(n1, n2)
# print(f"result = {result}")

# result = add(
#     int(input("enter value1: ")), 
#     int(input("enter value2: "))
# )
# print(f"result = {result}")

def function4():
    # function1 invocation
    function1()

    # function2 invocation
    function2(20)

    # function3 invocation
    function3(10, 20, 30)

# function4()

def function5(p1: int, p2: str, p3: bool):
    print(f"p1 = {p1}, type = {type(p1)}")
    print(f"p2 = {p2}, type = {type(p2)}")
    print(f"p3 = {p3}, type = {type(p3)}")

# indexed arguments (positional arguments)
# - parameters will be passed using their declaration position
# p1: 10, p2: "test", p3: False
# function5(10, "test", False)

# p1: "teset", p2: 10, p3: False
# function5("test", 10, False)

# named arguments
# - passing the parameters using the paramter names
# p1: 10, p2: "test", p3: False
# function5(p1=10, p2="test", p3=False)

# p1: 10, p2: "test", p3: False
# function5(p2="test", p1=10, p3=False)
# function5(p2="test", p3=False, p1=10)

# mixed style
# p1: 10, p2: "test", p3: False
# function5(10, p3=False, p2="test")
# function5(10, "test", p3=False)

# these statements will raise an error

# error: p2 is getting intialized twice
# function5(10, "test", p2=False)
# function5(10, "test", p2=False, p3=False)

# error: the indexed arguments must come before the named arguments
# function5(p1=10, "test", False)


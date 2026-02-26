# nested function
# - also known as local or inner function
# - function within a function
# - inner function can access all the members of outer function
#   - local variables and parameters and other inner functions of outer function
# - outer function can NOT access any member of inner function

# scope: global
def outer_function(param: int):
    print("inside outer_function")
    print(f"param = {param}")

    # scope: local
    my_var = 200
    print(f"my_var = {my_var}")

    # scope: local
    def inner_function1():
        print("inside inner_function1")

        # try accessing local variable
        print(f"my_var = {my_var}")

        # try accessing the outer function's parameter
        print(f"param = {param}")

        # scop: local
        inner_local_variable = 500
        print(f"inner_local_variable = {inner_local_variable}")
        print('-' * 80)

    # call the inner function
    # inner_function1()

    # try accessing the inner_function's members
    # print(f"inner_local_variable = {inner_local_variable}")

    def inner_function2():
        print("inside inner_function2")

        # scope: global
        global num
        num = 500

        # call other inner function
        inner_function1()

    # calling the inner function
    inner_function2()

outer_function(10)

# since my_var is a local variable of outer_function
# it can NOT be accessed outside of outer_function
# print(f"outside outer_function, my_var = {my_var}")

# since inner_function1 is a local function of outer_function
# it can be called only within outer_function
# inner_function1()


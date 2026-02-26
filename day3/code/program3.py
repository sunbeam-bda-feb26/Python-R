# scope of variable
# - global 
#   - variable declared outside any function
#   - variable declared inside a function with global keyword
#   - can be used anywhere in the program / file
# - local
#   - variable declared within a function
#   - can be used only within the function
# - global keyword
#   - used to declare a global variable inside a function
#   - to modify a global variable value within a function (local context)

# global variable
# global num
num = 200
print(f"before calling function, num = {num}")

# since my_var will be declared by function1, 
# you can NOT access this before function1()
# print(f"before calling function, num = {my_var}")

print('-' * 80)

def function1():
    print("inside function1")

    # scope: local
    salary = 25.50
    print(f"salary = {salary}")

    # scope: global
    global my_var
    my_var = 400
    print(f"my_var = {my_var}")

    # update the global variable
    global num
    num = 500
    print(f"num    = {num}")

    print('-' * 80)

function1()

print(f"after calling function, num = {num}")
print(f"after calling function, my_var = {my_var}")

# since the salary is a local variable of function1,
# it can be accessed only within function1
# print(f"after calling function, salary = {salary}")

print('-' * 80)
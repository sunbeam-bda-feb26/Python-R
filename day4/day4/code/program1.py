# nonlocal
# - keyword used to declare a member to update its value in inner_function
# - it lets the inner function update the outer function's member

def outer_function():
    print("inside outer_function")

    # scope: local
    my_var = 200
    print(f"my_var = {my_var}")

    my_var = 300
    print(f"my_var = {my_var}")
    print('-' * 80)

    def inner_function():
        print(f"inside inner_function")
        # declare the variable my_var as nonlocal
        nonlocal my_var
        
        # changing the value of my_var (outer_function's member)
        my_var = 400
        print(f"my_var = {my_var}")
        print('-' * 80)

    inner_function()
    print(f"my_var = {my_var}")
    print('-' * 80)

    def inner_function2():
        print(f"inside inner_function2")
        print(f"my_var = {my_var}")

    inner_function2()

outer_function()

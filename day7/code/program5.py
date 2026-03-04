def function1():
    # import math_operations from my_package
    import my_package.math_operations
    my_package.math_operations.add(10, 40)
    my_package.math_operations.subtract(10, 40)
    my_package.math_operations.divide(10, 40)
    my_package.math_operations.multiply(10, 40)

# function1()

def function2():
    # import math_operations from my_package with an alias
    import my_package.math_operations as mo

    mo.add(40, 50)
    mo.subtract(40, 50)
    mo.divide(40, 50)
    mo.multiply(40, 50)

# function2()

def function3():
    # import add from math_operations module from my_package
    from my_package.math_operations import add
    from my_package.math_operations import subtract
    from my_package.math_operations import divide, multiply

    add(40, 60)
    subtract(40, 50)
    divide(40, 50)
    multiply(40, 50)

# function3()

def function4():
    # import add from math_operations module from my_package
    from my_package.math_operations import add as mo_add
    from my_package.math_operations import subtract as mo_subtract
    from my_package.math_operations import divide as mo_divide, multiply as mo_multiply

    mo_add(40, 60)
    mo_subtract(40, 50)
    mo_divide(40, 50)
    mo_multiply(40, 50)

function4()
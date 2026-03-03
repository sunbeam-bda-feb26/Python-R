# variable length argument function
# - function which can accept variable length of arguments
# - accepts two parameters
#   - *args
#     - parameter of type tuple
#     - used to collect all the positional arguments
#     - args is NOT a keyword (instead of args, any other name can be used)
#   - **kwargs
#     - parameter of type dictionary
#     - used to collect all named arguments
#     - kwargs is NOT a keyword (instead of kwargs, any other name can be used)


def add(p1: int, p2: int, p3: int=0, p4: int=0, p5: int=0):
    print(f"inside add function")
    addition = p1 + p2 + p3 + p4 + p5
    print(f"addition = {addition}")

# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)
# add(10, 20, 30, 40, 50)

def function1(*args):
    print(f"inside function1")
    print(f"args     = {args}, type = {type(args)}")
    addition = 0
    for number in args:
        addition += number
    print(f"addition = {addition}")

# function1(10, 20)
# function1(10, 20, 30)
# function1(10, 20, 30, 40)
# function1(10, 20, 30, 40, 50)
# function1(10, 20, 30, 40, 50, 60)


def function2(*args, **kwargs):
    print(f"args   = {args}, type = {type(args)}")
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")

# function2(10, 20, operator="plus")
# function2(10, 20, 30, operator="star")

def function3(*args, **kwargs):
    # expectation
    # - kwargs provides the operator (plus/star)
    print(f"args   = {args}, type = {type(args)}")
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")

    # read the value of operator
    operator = kwargs['operator']
    if operator not in ['star', 'plus']:
        print("operator not supported")
    else:
        result = 0 if kwargs['operator'] == 'plus' else 1
        for number in args:
            if kwargs['operator'] == 'plus':
                result += number
            elif kwargs['operator'] == 'star':
                result *= number
            
        print(f"result = {result}")

# function3(10, 20, 30, operator='plus')
# function3(4, 6, 8, 9, 3, operator="star")
# function3(4, 6, 8, 9, 3, operator="divide")

def my_range(stop:int, *args):
    print(f"args = {args}")
    if len(args) > 2:
        print("more no of parameters passed")
    else:
        start = 0
        step = 1

        # check the number of variable arguments
        if len(args) == 1:
            start = stop
            stop = args[0]
        elif len(args) == 2:
            start = stop
            stop = args[0]
            step = args[1]

        print(f"start: {start}, stop: {stop}, step = {step}")

# start: 0, stop: 10, step = 1
my_range(10)

# start: 1, stop: 10, step = 1
my_range(1, 10)

# start: 1, stop: 10, step = 2
my_range(1, 10, 2)
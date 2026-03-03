# string formatting

def function1():
    # string
    text = "python"

    # without alignment the string
    print(f"without alignment     = {text}END")

    # with left alignment
    print(f"with left alignment   = {text:<15}END")

    # with right alignment
    print(f"with right alignment  = {text:>15}END")

    # with center alignment
    print(f"with center alignment = {text:^15}END")

# function1()

def function2():
    # string
    text = "python"

    # without alignment the string
    print(f"without alignment     = {text}END")

    # with left alignment
    print(f"with left alignment   = {text:-<15}END")

    # with right alignment
    print(f"with right alignment  = {text:*>15}END")

    # with center alignment
    print(f"with center alignment = {text:|^15}END")

# function2()

def function3():
    # int
    num = 20

    # print the value in decimal number system
    print(f"num      = {num}")
    print(f"num      = {num:8d}")
    print(f"num      = {num:08d}")
    print(f'-' * 80)

    # print the value in binary number system
    print(f"num      = {num:b}")
    print(f"num      = {num:8b}")
    print(f"num      = {num:08b}")
    print(f'-' * 80)

    # print the value in octal number system
    print(f"num      = {num:o}")
    print(f"num      = {num:8o}")
    print(f"num      = {num:08o}")
    print(f'-' * 80)

    # print the value in hexadecimal number system
    print(f"num      = {num:x}")
    print(f"num      = {num:8x}")
    print(f"num      = {num:08x}")
    print(f"num      = {num:X}")
    print(f"num      = {num:8X}")
    print(f"num      = {num:08X}")
    print(f'-' * 80)

# function3()

def function4():
    # float
    salary = 25.564677
    print(f"salary   = {salary}")

    # formatting the float value
    print(f"salary   = {salary:f}")
    print(f"salary   = {salary:.1f}")
    print(f"salary   = {salary:.2f}")
    print(f"salary   = {salary:.3f}")
    print(f"salary   = {salary:.4f}")

# function4()

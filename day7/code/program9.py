# menu driven application

def function1():
    print(f"inside function1")

def function2():
    print(f"inside function2")

def function3():
    print(f"inside function3")

def function4():
    print(f"inside function4")

def print_menu_and_get_choice():
    # print menu
    print(f"your options are:")
    print(f"1. function1")
    print(f"2. function2")
    print(f"3. function3")
    print(f"4. function4")
    print(f"q. quit")

    # get the input from user
    choice = input("enter your choice: ")
    return choice

# start a infinite loop
while True:

    # print the menu and get choice from user
    ch = print_menu_and_get_choice()

    # check the choice and perform respective operation
    if ch == '1':
        function1()
    elif ch == '2':
        function2()
    elif ch == '3':
        function3()
    elif ch == '4':
        function4()
    elif ch == 'q':
        # break the loop and stop the application
        break
    else:
        print("invalid choice")

print("bye bye..")

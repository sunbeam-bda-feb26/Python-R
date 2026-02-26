# type()
# - used to get the data type assigned to a variable

# integer variable (whole number)
num = 200
print(f"num              = {num}, type = {type(num)}")

# float variable (decimal number)
salary = 25.50
print(f"salary           = {salary}, type = {type(salary)}")

# complex variable (real and imaginary number)
complex_variable = 20 + 5j
print(f"complex_variable = {complex_variable}, type = {type(complex_variable)}")

print('-' * 80)

# string with single line value
first_name = "steve"
print(f"first_name       = {first_name}, type = {type(first_name)}")

# string with single line value
last_name = 'jobs'
print(f"last_name        = {last_name}, type = {type(last_name)}")


# string with multi line value
new_address = "house number 100,\n" \
"Pune,\n"\
"Maharashtra 411041"
print(f"new_address      = {new_address}, type = {type(new_address)}")

# string with multilines value
address = """house number 100,
Pune, 
Maharashtra 411041"""
print(f"address          = {address}, type = {type(address)}")

# string with multilines value
address = '''house number 100,
Pune, 
Maharashtra 411041'''
print(f"address          = {address}, type = {type(address)}")

# string with a single character
ch = 'a'
print(f"ch = {ch}, type = {type(ch)}")

print('-' * 80)

# boolean variable
can_vote = True
print(f"can_vote         = {can_vote}, type = {type(can_vote)}")

print('-' * 80)

# none type variable
my_var = None
print(f"my_var           = {my_var}, type = {type(my_var)}")

print('-' * 80)

# list: mutable collection
numbers_list = [10, 20, 30, 40, 50]
print(f"numbers_list     = {numbers_list}, type = {type(numbers_list)}")

# tuple: immutable collection
# numbers_tuple = (10, 20, 30, 40, 50)
numbers_tuple = 10, 20, 30, 40, 50  # tuple packing
print(f"numbers_tuple    = {numbers_tuple}, type = {type(numbers_tuple)}")

# set: collection of unique values
numbers_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
print(f"numbers_set      = {numbers_set}, type = {type(numbers_set)}")

# dictionary: collection of key-value pairs
person = {"name": "person1", "age": 30, "address": "pune"}
print(f"person           = {person}, type = {type(person)}")


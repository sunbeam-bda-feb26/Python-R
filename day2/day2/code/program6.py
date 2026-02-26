# type conversion
# - float(): used to convert anything to float
# - int(): used to convert anything to int
# - str(): used to convert anything to string without any exception
# - bool(): used to convert anything to bool
# - list(): used to convert any collection to list
# - tuple(): used to convert any collection to tuple
# - set(): used to convert any collection to set
# - dict(): used to convert any collection to dictionary

# convert anything to float

num = 200
print(f"num       = {num}, type = {type(num)}")

# int to float
num_float = float(num)
print(f"num_float = {num_float}, type = {type(num_float)}")

# string to float
num_float = float('35.50')
print(f"num_float = {num_float}, type = {type(num_float)}")

# string to float: fails with rasing an exception - ValueError 
# num_float = float('test')
# print(f"num_float = {num_float}, type = {type(num_float)}")

# string to float: fails with an exception: ValueError
# num_float = float('45.6test')
# print(f"num_float = {num_float}, type = {type(num_float)}")

# bool to float
num_float = float(True)
print(f"num_float = {num_float}, type = {type(num_float)}")

# bool to float
num_float = float(False)
print(f"num_float = {num_float}, type = {type(num_float)}")

print('-' * 80)

# float to int: lossy conversion
num_int = int(35.50)
print(f"num_int = {num_int}, type = {type(num_int)}")

# string to int
num_int = int("10")
print(f"num_int = {num_int}, type = {type(num_int)}")

# string to int: fails with an exception: ValueError
# num_int = int("test")
# print(f"num_int = {num_int}, type = {type(num_int)}")

# bool to int
num_int = int(True)
print(f"num_int = {num_int}, type = {type(num_int)}")

print('-' * 80)

# int to string
num_str = str(1000)
print(f"num_str = {num_str}, type = {type(num_str)}")

# float to string
num_str = str(1000.40)
print(f"num_str = {num_str}, type = {type(num_str)}")

# bool to string
num_str = str(True)
print(f"num_str = {num_str}, type = {type(num_str)}")
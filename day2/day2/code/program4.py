# dynamic typing
# - data type will be assigned at the run time

n1 = 200
print(f"n1 = {n1}, type = {type(n1)}, id = {id(n1)}")

n1 = 300
print(f"n1 = {n1}, type = {type(n1)}, id = {id(n1)}")

print('-' * 80)

# int
num = 200
print(f"num = {num}, type = {type(num)}, id = {id(num)}")

num1 = num + 200
print(f"num1 = {num1}, type = {type(num1)}, id = {id(num1)}")

# float
num = 25.50
print(f"num = {num}, type = {type(num)}, id = {id(num)}")

num1 = num + 200
print(f"num1 = {num1}, type = {type(num1)}, id = {id(num1)}")

# bool
num = True
print(f"num = {num}, type = {type(num)}, id = {id(num)}")

num1 = num + 200
print(f"num1 = {num1}, type = {type(num1)}, id = {id(num1)}")

# complex
num = 20 + 5j
print(f"num = {num}, type = {type(num)}, id = {id(num)}")

num1 = num + 200
print(f"num1 = {num1}, type = {type(num1)}, id = {id(num1)}")

# str
num = "sunbeam"
print(f"num = {num}, type = {type(num)}, id = {id(num)}")

# num1 = num + 200
# print(f"num1 = {num1}, type = {type(num1)}, id = {id(num1)}")

print('-' * 80)

# providing a type hinting to the IDE/editor
# type hint is an optional feature
my_var: int = 200
print(f"my_var = {my_var}, type = {type(my_var)}")

my_var = "test"
print(f"my_var = {my_var}, type = {type(my_var)}")


# get input from user

# the entered value will be stored in name variable
name = input("enter your name: ")
print(f"name = {name}, type = {type(name)}")


# accept the age in string and convert it into an integer value
age = int(input("enter your age: "))
print(f"age = {age}, type = {type(age)}")

address = input("enter your address: ")
print(f"address = {address}, type = {type(address)}")

# if (age >= 18) {
# }

# block
# - group of statements
# - starts with colon (:)
# - the statements must appear on the next line with an indentation
# - python uses indentation for block creation

# check if age is greater than 18
if age >= 18:
    # YES
    print("person is eligible")
    print("second line in if block")
else:
    # NO
    print("person is NOT eligible")
    print("second line in else block")

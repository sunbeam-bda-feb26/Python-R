# object
# - also known as an instance
# - collection of 
#   - data members: fields, attributes, properties
#   - member functions: methods (function defined inside a class)
# - can be created using class
# - characteristics
#   - state
#     - values stored in the object members (attributes)
#     - e.g. person1's state => {first_name: john, last_name: doe}
#   - id
#     - every object will be identified uniquely using a unique address
#     - every object gets a unique memory address
# - e.g. renault triber with white color

# class
# - blueprint or template to create an object
# - collection of 
#   - data members: fields, attributes, properties
#   - member functions: methods
# - implemented using a 'class' keyword
# - e.g. Car

# empty class definition
class Person:
    """this is a dummy class"""
    pass

# print(f"docstring of Person = {Person.__doc__}")

# instantiation
# - create an object of Person class
# - 'new' is not a keyword is python and is not used to create an object
# - syntax
#   - <reference> = <class name>()

# person1 is reference to an object
# Person() will create an object
person1 = Person()
print(f"person1             = {person1}, type = {type(person1)}")

# __dict__: attribute used to get the contents of an object in dictionary format
print(f"contents of person1 = {person1.__dict__}")

# add an attribute to the object
setattr(person1, "first_name", "john")
print(f"contents of person1 = {person1.__dict__}")

# add an attribute
setattr(person1, "last_name", "doe")
print(f"contents of person1 = {person1.__dict__}")

# add an attribute
setattr(person1, "address", "usa")
print(f"contents of person1 = {person1.__dict__}")


print('-' * 80)

# person2 is reference to an object
# Person() will create an object
person2 = Person()
print(f"person2             = {person2}, type = {type(person2)}")
print(f"contents of person2 = {person2.__dict__}")

# add an attribute to the object
setattr(person2, "first_name", "jane")
print(f"contents of person2 = {person2.__dict__}")

# add an attribute
setattr(person2, "last_name", "doe")
print(f"contents of person2 = {person2.__dict__}")

# add an attribute
setattr(person2, "present_address", "USA")
print(f"contents of person2 = {person2.__dict__}")

# this line will create an object without any reference
# such object without any reference is known as anonymous object
# Person()



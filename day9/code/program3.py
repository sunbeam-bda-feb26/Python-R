# abstraction
# - hiding the internal details of the class implementation
# - implemented by using access modifiers

# access specifier/modifier
# - how the access to the members is provided
# - python does not provide any keyword to specify the access
# - instead, python uses conventions
# - public
#   - member can be accessed/modified outside the class
#   - convention: do not use any _ prefix
# - protected
#   - member can be accessed/modified within the class and 
#     all child classes of the class
#   - convention: use single underscore(__) as prefix
# - private
#   - member can be accessed/modified only within the same class
#   - member can NOT be accessed/modified outside the class
#   - convention: use double underscore (__) as prefix

class Person:
    def __init__(self, name: str, age: int):
        # set the values to name and age attributes

        # public
        self.name = name

        # private
        self.__age = age

    # getter for age
    def get_age(self):
        return self.__age
    
    # setter for age
    def set_age(self, age: int):
        # validation
        if age > 20 and age < 60:
            self.__age = age
        else:
            print(f"invalid age")

    # facilitator
    def can_vote(self):
        if self.__age >= 18:
            print(f"{self.name} is eligible for voting")
        else:
            print(f"{self.name} is NOT eligible for voting")

p1 = Person('person1', 30)
# print(f"p1 = {p1.__dict__}")
print(f"name = {p1.name}, age = {p1.get_age()}")

# NOTE
# - this line wont produce any error
# - this line wont change the value of __age either
# p1.__age = 45

# Person.set_age(p1, 45)
p1.set_age(45)
print(f"name = {p1.name}, age = {p1.get_age()}")

# compiler converts this code
# Person.can_vote(p1)
p1.can_vote()
print('-' * 80)

p2 = Person('person2', 10)
# print(f"p2 = {p2.__dict__}")
print(f"name = {p2.name}, age = {p2.get_age()}")
# p2.__age = -180

# Person.set_age(p2, 45)
p2.set_age(-180)
print(f"name = {p2.name}, age = {p2.get_age()}")

# compiler converts this code
# Person.can_vote(p2)
p2.can_vote()
print('-' * 80)

# anonymous object
# a new memory gets allocated for the object
# the reference of this memory is captured
# the __init__ of the class is called by passing the memory address
# - Person.__init__(<memory address of newly created object>) 
Person("person3", 50).can_vote()
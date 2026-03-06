# inheritance
# - a class sharing public and protected attributes and methods with child class(es)
# - private members of super class will NOT be shared with subclass
# - also known as is-a relationship
# - type
#   - single inheritance
#     - there is a single parent and a child class

# object class
# - python 3.0 has introduced the object class as a root class
# - root class of python which is the base class of all classes in python
# - every class in python is derived from object directly or indirectly
# - provides
#   - memory management feature to all the classes
#   - default implmentations of utility methods like __str__ etc.


# Person is superclass of Employee
# Person is base class of Employee
# Person is parent class of Employee
class Person:
# class Person():
# class Person(object):
    def __init__(self):
        self.name = "person1"
        self.age = 30
    
    def person_method(self):
        print(f"called from Person")

# Employee is-a Person
# Employee is derived from Person
# Employee is inherited from Person

# Employee is a subclass of Person
# Employee is a derived class of Person
# Employee is a child class of Person
class Employee(Person):
    pass

print(f"base class of Person   = {Person.__base__}")
print(f"base class of Employee = {Employee.__base__}")
print('-' * 80)

person = Person()
print(f"person contents   = {person.__dict__}")
person.person_method()
print('-' * 80)

employee = Employee()
print(f"employee contents = {employee.__dict__}")

# since Employee is derived class of Person
# Person class methods can be called from employee object
employee.person_method()
print('-' * 80)

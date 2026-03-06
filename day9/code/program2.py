# class
# - encapsulation
#   - bringing both data members and methods together in one single entity
# - data members: used to store the data
# - member functions (methods)
#   - static methods
#     - associated with the class
#     - can be called directly using a class 
#     - does not require any object to be created
#   - non-static method
#     - must be called only by using an object
#     - every non-static method must accept the first parameter as
#       reference of the current object (self)
#     - initializer
#       - special method of class which is used to initialize an object
#       - in python, initializer method name must be __init__
#       - similar to constructor in other languages
#       - every class must have an initializer
#         - if an explicit initializer is not provided by the class, 
#           compiler adds a defualt initializer (__init__(self))
#         - if an explicit initializer is provided, compiler does NOT 
#           add any default initializer
#       - gets called automatically or implicitly for every object 
#     - de-initializer
#       - similar to destructor in other language
#       - used to de-initialize the object
#       - used to release the resources which are accumulated by the object
#       - name of the de-initializer is __del__
#       - every class must have an de-initializer
#         - if an explicit de-initializer is not provided by the class, 
#           compiler adds a defualt de-initializer (__del__(self))
#         - if an explicit de-initializer is provided, compiler does NOT 
#           add any default de-initializer
#       - gets called automatically or implicitly for every object just before
#         the object gets deleted / destroyed from the memory
#     - setter or mutator
#       - used to set value of an attribute
#       - implemented for individual attributes
#       - start the method name with 'set_'
#     - getter or inspector
#       - method used to get value of an attribute
#       - implemented for individual attributes
#       - start the method name with 'get_'
#     - facilitator
#       - used to add a facility in the class

# self
# - parameter of every non-static method
# - a reference of current object which is used to call the method
# - is NOT a keyword, it is a convention
# - similar to 'this' keyword in other languages

# garbage collection
# - known as automatic memory management
# - it deletes the object which is not required
#   - e.g. anonymous object gets deleted immediately
# - all the objects will be deleted at the end of the program
# - but if required, an object can be deleted explicitly using del keyword

class Person:
    # explicit initializer
    def __init__(self):
        print(f"inside __init__(), self = {self}")

    # explicit de-initializer
    def __del__(self):
        print(f"inside __del__(), self = {self}")

# instantiation
# a new memory gets allocated for the object
# the reference of this memory is captured in p1
# the __init__ of the class is called by passing the reference (p1)
# - Person.__init__(p1) : please do not write this code
p1 = Person()
print(f"p1 = {p1}, type = {type(p1)}")

# explicitly delete p1
del p1

print('-' * 80)

# instantiation
# a new memory gets allocated for the object
# the reference of this memory is captured in p2
# the __init__ of the class is called by passing the reference (p2)
# - Person.__init__(p2) : please do not write this code
p2 = Person()
print(f"p2 = {p2}, type = {type(p2)}")
print('-' * 80)

# instantiation
# the below line will create an anonymous object which will be 
# destroyed immediately after this line since there is no reference
# for this object and it can NOT be used again
Person()
print('-' * 80)

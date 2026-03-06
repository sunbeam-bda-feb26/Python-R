# association using agreegation
# - weak relationship or loose coupling
# - both the classes can live without each other
# - e.g. Person has-a Car, Company has-an Employee

class Car:
    def __init__(self, model: str, price: int):
        self.__model = model
        self.__price = price

    def print_car_info(self):
        print(f"model = {self.__model}")
        print(f"price = {self.__price}")

class Person:
    def __init__(self, name: str, address: str, car: Car):
        self.__name = name
        self.__address = address

        # person has-a car
        self.__car = car

    def print_person_info(self):
        print(f"name = {self.__name}, address = {self.__address}")

        # since the __car is a refrence to a Car class object
        # to get the details, call print_car_info method
        if self.__car is not None:
            self.__car.print_car_info()


# create a car class object
car = Car("triber", 12)

# create a person class object
person = Person("person1", "pune", car)

# print person details
person.print_person_info()


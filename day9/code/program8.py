# Note
# - if a super class has explicit initializer method implemented
#   it is mandatory for subclass to implement its initializer method
#   and class the super class initializer method to initialize super class


class Vehicle:
    # eplicit intializer
    def __init__(self, engine_name: str):
        self._engine_name = engine_name
    
    def print_vehicle_details(self):
        print(f"engine name = {self._engine_name}")


class Car(Vehicle):

    # initializer for Car
    def __init__(self, engine_name, model, company):
        
        # initialize the super class
        Vehicle.__init__(self, engine_name)

        # save the car properties
        self.__model = model
        self.__company = company
    
    def print_car_details(self):
        print(f"model       = {self.__model}")
        print(f"company     = {self.__company}")
        print(f"engine name = {self._engine_name}")

car = Car("v1.2", "i10", "hyundai")
car.print_car_details()
# associate with composition 
# - strong relationship or tight coupling
# - object can NOT live with each other
# - e.g. Car is composed-of Engine (Car has-an Engine)

class Engine:
    def __init__(self, name: str, fuel_type: str):
        self.__name = name
        self.__fuel_type = fuel_type

    def print_engine_info(self):
        print(f"name      = {self.__name}")
        print(f"fuel type = {self.__fuel_type}")

class Car:
    def __init__(self, model: str, price: int, engine_name: str, fuel_type: str):
        # save the car details
        self.__model = model
        self.__price = price

        # create an object of Engine
        self.__engine = Engine(engine_name, fuel_type)

    def __del__(self):
        # since there is a strong relationship between Car and Engine
        # lets delete engine when the car is getting deleted
        del self.__engine

    def print_car_info(self):
        print(f"model = {self.__model}, price = {self.__price}")

        # since the __engine is a reference of Engine class
        # call print_engine_info method to get the details
        self.__engine.print_engine_info()
    
car = Car("triber", 12, "renault-engine", 'EV')

car.print_car_info()
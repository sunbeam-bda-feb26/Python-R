class Car:
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def print_car_info(self):
        print(f"model   = {self.__model}")
        print(f"company = {self.__company}")
        print(f"price   = {self.__price}")
        print('-' * 80)

car1 = Car("i10", "hyundai", 10)
car1.print_car_info()

# car2 = Car('triber', 'renault', 12)
# car2.print_car_info()

# create a new car using existing car
# reference is copied (both the references are referring the same object)
car2 = car1
car2.print_car_info()

car1.set_price(15)
car1.print_car_info()
car2.print_car_info()

print('-' * 80)

# object of int class
num1 = 200
print(f"num1 = {num1}, type = {type(num1)}")

# object of int class
num2 = num1
print(f"num2 = {num2}, type = {type(num2)}")

num1 = 300
print(f"num1 = {num1}, type = {type(num1)}")
print(f"num2 = {num2}, type = {type(num2)}")
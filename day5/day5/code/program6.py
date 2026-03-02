# map()
# - transformation function
# - used to transform every value in a collection to something new
# - accepts two paramesters
#   - reference to the transformation function
#   - collection on which the transformation function needs to be called
# - logic of map
#   - internally iterates the collection (2nd parameter)
#   - for every iteration, it calls the transformation function by passing 
#     the value at that iteration
#   - the return value of transformation function gets collected inside a collection
#   - returns a collection with all transformed values
# - returns
#   - always returns a collection with transformed values
#   - the size of the return value (collection) will be same as that of the 
#     original collection

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # get square of every number and store it in another collection

    # step1: create an empty collection
    squares = []

    # step2: iterate over the collection and get square of each of the numbers
    for number in numbers:
        # get the square
        square = number ** 2

        # append the square to the squares list
        squares.append(square)

    # print all the squares
    print(f"squares = {squares}")

# function1()

def function2():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # get square of every number -> transformation 
    # and store it in another collection

    # step1: create an empty collection
    squares = []

    # step2: implement transformation function
    # def square(number):
    #     return number ** 2

    # step2: implement transformation lambda function
    square = lambda n: n ** 2

    # step3: iterate over the collection and get square of each of the numbers
    for number in numbers:
        # get the square
        square_value = square(number)

        # append the square to the squares list
        squares.append(square_value)

    # print all the squares
    print(f"squares = {squares}")

# function2()

def function3():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # get square of every number -> transformation 
    # and store it in another collection
    square = lambda n: n ** 2
    # def square(number):
    #     print(f"number = {number}")
    #     return number ** 2

    # get the square of every number
    squares = list(map(square, numbers))
    print(f"squares = {squares}")

# function3()

def function4():
    # list of temperatures in celsius
    temperatures = [20, 30, 41, 23, 29, 48, 29]
    print(f"temperatures            = {temperatures}")

    # convert all these temperatures in fahrenheit
    # temperatures_fahrenheit = []
    # for temperature in temperatures:
    #     # transform the celsius in fahrenheit
    #     temperature_f = 32 + (temperature * (9/5))

    #     # collect the new temperature to the temperature collection
    #     temperatures_fahrenheit.append(temperature_f)
    # print(f"temperatures_fahrenheit = {temperatures_fahrenheit}")

    # step1: write tranformation function
    to_fahrenheit = lambda t: 32 + (t * (9/5))

    # step2: call map and the new tempertures
    temperatures_fahrenheit = list(map(to_fahrenheit, temperatures))
    print(f"temperatures_fahrenheit = {temperatures_fahrenheit}")
    
# function4()

def function5():
    # distance in meters
    distances_meters = [10, 20, 34, 50, 60, 90, 100]

    # transformation function
    to_cm = lambda d: d * 100

    # convert all the distances from meters to centimeters
    distances_centimeters = tuple(map(to_cm, distances_meters))
    print(f"distances in meters = {distances_meters}")
    print(f"distances in cm     = {distances_centimeters}")

# function5()

def function6():
    # list of dictionaries
    cars = [
        {
            "id": 1,
            "brand": "Toyota",
            "model": "Fortuner",
            "year": 2023,
            "price": 4200000,
            "fuel_type": "Diesel",
            "transmission": "Automatic",
            "mileage_kmpl": 14.2,
            "color": "White",
            "is_available": True
        },
        {
            "id": 2,
            "brand": "Hyundai",
            "model": "Creta",
            "year": 2022,
            "price": 1800000,
            "fuel_type": "Petrol",
            "transmission": "Manual",
            "mileage_kmpl": 17.4,
            "color": "Black",
            "is_available": True
        },
        {
            "id": 3,
            "brand": "Tata",
            "model": "Nexon",
            "year": 2024,
            "price": 1500000,
            "fuel_type": "Electric",
            "transmission": "Automatic",
            "mileage_kmpl": 0,
            "color": "Blue",
            "is_available": False
        },
        {
            "id": 4,
            "brand": "Mahindra",
            "model": "Scorpio N",
            "year": 2023,
            "price": 2200000,
            "fuel_type": "Diesel",
            "transmission": "Automatic",
            "mileage_kmpl": 15.0,
            "color": "Red",
            "is_available": True
        },
        {
            "id": 5,
            "brand": "Honda",
            "model": "City",
            "year": 2021,
            "price": 1300000,
            "fuel_type": "Petrol",
            "transmission": "CVT",
            "mileage_kmpl": 18.4,
            "color": "Silver",
            "is_available": True
        },
        {
            "id": 6,
            "brand": "Maruti Suzuki",
            "model": "Baleno",
            "year": 2022,
            "price": 900000,
            "fuel_type": "Petrol",
            "transmission": "Manual",
            "mileage_kmpl": 22.3,
            "color": "Grey",
            "is_available": False
        },
        {
            "id": 7,
            "brand": "Kia",
            "model": "Seltos",
            "year": 2023,
            "price": 1900000,
            "fuel_type": "Diesel",
            "transmission": "Automatic",
            "mileage_kmpl": 16.5,
            "color": "Orange",
            "is_available": True
        },
        {
            "id": 8,
            "brand": "BMW",
            "model": "X1",
            "year": 2024,
            "price": 4900000,
            "fuel_type": "Petrol",
            "transmission": "Automatic",
            "mileage_kmpl": 14.8,
            "color": "White",
            "is_available": True
        },
        {
            "id": 9,
            "brand": "Mercedes-Benz",
            "model": "C-Class",
            "year": 2023,
            "price": 6000000,
            "fuel_type": "Petrol",
            "transmission": "Automatic",
            "mileage_kmpl": 13.0,
            "color": "Black",
            "is_available": False
        },
        {
            "id": 10,
            "brand": "Audi",
            "model": "A4",
            "year": 2022,
            "price": 5500000,
            "fuel_type": "Petrol",
            "transmission": "Automatic",
            "mileage_kmpl": 14.1,
            "color": "Blue",
            "is_available": True
        }
    ]

    # transformation function
    # to_new_car = lambda car: {"brand": car['brand'], "model": car['model'], "price": car['price']}

    # get every car's brand, model and price
    # projection: select brand, model, price from cars
    # new_cars = list(map(to_new_car, cars))
    # print(f"car      = {cars}")
    # print('-' * 80)
    # print(f"new_cars = {new_cars}")

    # get models of all cars
    to_car_model = lambda car: car['model']
    models = list(map(to_car_model, cars))
    print(f"models = {models}")

function6()



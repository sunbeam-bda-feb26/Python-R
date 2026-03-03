# list comprehension
# - better syntax used to implement the map and filter
# - always returns a list
# - syntax
#   - [<return expression> <for loop> <filter condition>]
#   - "return expression" and "for loop" are mandatory 
#     while the "filter condition" is optional
# - when the filter condition is missing, the list comprehension acts as a map
# - when the filter condition is present, the list comprehension acts as a filter

# single line if-else condition
# - syntax
#   - <return value for if block> if <condition> else <return value of else block>

def function1():
    # list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}")

    # get square of each number
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    print(f"squares = {squares}")

    # get square of each number
    squares = list(map(lambda n: n ** 2, numbers))
    cubes = list(map(lambda n: n ** 3, numbers))
    print(f"squares = {squares}")
    print(f"cubes   = {cubes}")

    # get square of each number
    squares = [n ** 2 for n in numbers]
    print(f"squares = {squares}")

    # get cube of each number
    cubes = [n ** 3 for n in numbers]
    print(f"cubes   = {cubes}")

# function1()

def function2():
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
    temperatures_fahrenheit = [32 + (t * (9/5)) for t in temperatures]
    print(f"temperatures_fahrenheit = {temperatures_fahrenheit}")

# function2()

def function3():
    # list of marks
    marks = [20, 30, 45, 10, 8, 45, 34, 29]
    print(f"students marks  = {marks}")
    
    # print whether a student is passed in the exam
    result = [m >= 15 for m in marks]
    print(f"result          = {result}")

    # print result of every student
    result = ['Pass' if m >= 15 else 'Fail' for m in marks]
    print(f"result          = {result}")

# function3()

def function4():
    # list of numbers
    numbers = [10, 13, 58, 90, 24, 27, 33, 30, 47]
    print(f"numbers      = {numbers}")

    # find only even numbers from the numbers collection
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(f"even numbers = {even_numbers}") 

    # find only even numbers from the numbers collection
    even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
    odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
    print(f"even numbers = {even_numbers}") 
    print(f"odd numbers  = {odd_numbers}") 

    # find only even numbers from the numbers collection
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    print(f"even numbers = {even_numbers}") 
    print(f"odd numbers  = {odd_numbers}") 
    
# function4()

def function5():
    # list of numbers   
    numbers = [10, 13, 58, 90, 24, 27, 33, 30, 47]
    print(f"numbers                = {numbers}")

    # find square of all even numbers
    even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
    square_even_numbers = list(map(lambda n: n ** 2, even_numbers))
    print(f"square of even numbers = {square_even_numbers}")

    # find square of all even numbers
    square_even_numbers = [n ** 2 for n in numbers if n % 2 == 0]
    print(f"square of even numbers = {square_even_numbers}")

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

    # list of car models (list comprehension acting like a map())
    models = [car['model'] for car in cars]
    print(f"models                    = {models}")
    print('-' * 80)

    # list of car brand, model and price (list comprehension acting like a map()) 
    car_info = [ {"brand": car['brand'], "model": car['model'], "price": car['price']} for car in cars]
    print(f"car info                  = {car_info}")
    print('-' * 80)

    # find the affordable cars (list comprehension acting like a filter())
    affordable_cars = [car for car in cars if car['price'] <= 2000000]
    print(f"affordable cars           = {affordable_cars}")
    print('-' * 80)

    # find the available cars
    available_cars = [car for car in cars if car['is_available']]
    print(f"available cars            = {available_cars}")
    print('-' * 80)

    # get non affordable car models
    non_affordable_car_models = [car['model'] for car in cars if car['price'] > 2000000]
    print(f"non affordable car models = {non_affordable_car_models}")
    
function6()
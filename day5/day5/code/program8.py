# filter()
# - selection function
# - used to select the values based on certain condition/criteria
# - accepts two paramesters
#   - reference to the selection function
#   - collection on which the selection function needs to be called
# - selection function must return a boolean result
# - logic of filter()
#   - internally iterates the collection (2nd parameter)
#   - for every iteration, it calls the selection function by passing 
#     the value at that iteration
#   - if the selection function returns True, the original number gets
#     added to the new collection
#   - returns a collection with selected values

def function1():
    # list of numbers
    numbers = [10, 13, 58, 90, 24, 27, 33, 30, 47]
    print(f"numbers      = {numbers}")

    # find only even numbers from the numbers collection
    even_numbers = []
    for number in numbers:
        # check if the number is even
        if number % 2 == 0:
            # add the number to even_numbers collection
            even_numbers.append(number)

    print(f"even numbers = {even_numbers}") 

# function1()

def function2():
    # list of numbers
    numbers = [10, 13, 58, 90, 24, 27, 33, 30, 47]
    print(f"numbers      = {numbers}")

    # write a function for selecting the number
    # def is_even(number):
    #     return number % 2 == 0
    is_even = lambda n: n % 2 == 0

    # find only even numbers from the numbers collection
    even_numbers = []
    for number in numbers:
        # check if the number is even
        if is_even(number):

            # add the number to even_numbers collection
            even_numbers.append(number)

    print(f"even numbers = {even_numbers}") 

# function2()


def function3():
    # list of numbers
    numbers = [10, 13, 58, 90, 24, 27, 33, 30, 47]
    print(f"numbers      = {numbers}")

    # write a function for selecting the number
    is_even = lambda n: n % 2 == 0

    # find only even numbers from the numbers collection
    even_numbers = list(filter(is_even, numbers))
    print(f"even numbers = {even_numbers}") 

# function3()

def function4():
    # list of marks
    marks = [20, 30, 45, 10, 8, 45, 34, 29]
    print(f"students marks  = {marks}")

    # find the students who passed in the exam (passing score is 15)
    is_passed = lambda m: m >= 15

    passed_students = list(filter(is_passed, marks))    
    print(f"students passed = {passed_students}")

# function4()
                               

def function5():
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

    # selection function
    # is_available = lambda car: car['is_available']

    # find the cars which are not avaiable
    # available_cars = list(filter(is_available, cars))
    # print(f"available cars = {available_cars}")

    # selection function
    is_affordable = lambda car: car['price'] <= 2000000

    # find the affordable cars (price <= 2000000)
    affordable_cars = list(filter(is_affordable, cars))
    print(f"affordable cars = {affordable_cars}")
    print(f'-' * 80)

    # get model and brand of affordable cars
    to_new_car = lambda car: f"{car['brand']} - {car['model']}"

    affordable_cars_info = list(map(to_new_car, affordable_cars))
    print(affordable_cars_info)

function5()

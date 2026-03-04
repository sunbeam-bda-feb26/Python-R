# json module
# - JSON: JavaScript Object Notation
# - formatting syntax to keep the configurations
# - contains
#   - object: similar to dictionary, e.g. {"name": "person1"} 
#   - array: similar to list, e.g. [10, 20, 30, 40] or [{"name": "person1", "age": 30}]

import json

def function1():
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

    # open a file in write mode to save the object
    with open("cars.json", "w") as file:
        # save the contents to a json file
        json.dump(cars, file)

# function1()

def function2():
    # open the file in read mode 
    with open("cars.json", "r") as file:

        # read the contents of the file in JSON format 
        # and convert it into list of dictionaries
        cars = json.load(file)

        print('-' * 77)
        print(f"| {'model':<15} | {'brand':<15} | {'price':>8} | {'fuel_type':<10} | {'transmission':<13} |")
        print('-' * 77)
        for car in cars:
            print(f"| {car['model']:<15} | {car['brand']:<15} | {car['price']:>8} | {car['fuel_type']:<10} | {car['transmission']:<13} |")
        print('-' * 77)

# function2()
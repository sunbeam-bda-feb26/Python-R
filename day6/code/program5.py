# string
# - immutable: once created, string can not be appended with new character
# - collection/sequence of characters
# - methods
#   - lower(): used to convert all the characters to their lower case
#   - upper(): used to convert all the characters to their upper case
#   - title(): first letter of every word gets upper cased and rest of the
#     letter will be in lower case
#   - replace(): 
#     - used to replace first parameter with the second parameter
#     - does not update the existing string, instead it returns a new string
#   - split(): used to split the string into multiple parts
#   - join(): used to create a string from mulitple parts (list)

def function1():
    # string
    text = "PytHon ProgrammING"
    print(f"text        = {text}")

    # convert all the characters to lower case
    print(f"lower cased = {text.lower()}")

    # convert all the characters to the upper case
    print(f"upper case  = {text.upper()}")

    # convert the string to the title case
    print(f"title case  = {text.title()}")

# function1()

def function2():
    # string
    text = "python programming"
    print(f"text                       = {text}")

    # positive indexing
    print(f"character at 0th position  = {text[0]}")
    print(f"character at 1st position  = {text[1]}")
    print(f"character at 2nd position  = {text[2]}")
    print(f"character at 3rd position  = {text[3]}")
    print(f"character at 4th position  = {text[4]}")
    print(f"character at 5th position  = {text[5]}")
    print('-' * 80)

    # negative indexing
    print(f"character at -1st position = {text[-1]}")
    print(f"character at -2nd position = {text[-2]}")
    print(f"character at -3rd position = {text[-3]}")
    print(f"character at -4th position = {text[-4]}")
    print(f"character at -5th position = {text[-5]}")
    
# function2()

def function3():
    # string
    text = "python programming"
    print(f"text       = {text}")
    print('-' * 80)

    # substring: extract the word python
    print(f"text[0:6]  = {text[0:6]}")
    print(f"text[:6]   = {text[:6]}")
    print('-' * 80)

    # extract the word programming
    print(f"text[7:18] = {text[7:18]}")
    print(f"text[7:]   = {text[7:]}")

# function3()

def function4():
    # string
    text = "I love Java programming. Java is a very simple language."
    print(f"text = {text}")

    # replace the word Java with Python
    print(f"text = {text.replace('Java', 'Python')}")

# function4()

def function5():
    # string
    text = "I love Java programming. Java is a very simple language."
    print(f"text  = {text}")

    # split the string into multiple parts using space as a splitting character
    parts = text.split()
    print(f"parts = {parts}")
    print('-' * 80)

    # string
    url = "https://google.co.in/search?q=python&location=india"

    # url: 
    # - uniform resource locator
    # - used to locate the resources uniquely
    # - resource: any file hosted on the web server
    # - components
    #   - scheme: protocol used to communicate with the server
    #   - domain name or ip address
    #     - domain name is the name assigned to an ip address
    #   - port number: of the server process running on the server machine
    #     - http: 80
    #     - https: 443
    #   - file name or path: of the resource to be located
    #   - query string: used to pass input values to the page
    #   - hash/proxy component: used to link section within a page

    # split the string for extracting the scheme
    scheme, remaining_url = url.split("://")
    print(f"scheme           = {scheme}, remaining_url = {remaining_url}")
    
    # split the string for extracting the domain name
    domain_name, remaining_url = remaining_url.split('/')
    print(f"domain name      = {domain_name}, remaining_url = {remaining_url}")

    # split the string for extracting the path
    path, remaining_url = remaining_url.split('?')
    print(f"path             = {path}, remaining_url = {remaining_url}")

    # split the string for extracting the query parameter names
    query_parameter1, query_parameter2 = remaining_url.split('&')
    print(f"query_parameter1 = {query_parameter1}")
    print(f"query_parameter2 = {query_parameter2}")

# function5()

def function6():
    # list of strings
    parts = ['I', 'love', 'python', 'programming']
    print(f"parts              = {parts}")

    # join the parts to form a string
    print(f"joining with space = {' '.join(parts)}")
    print(f"joining with -     = {'-'.join(parts)}")
    print(f"joining with *     = {'*'.join(parts)}")
    print(f"joining with -*-   = {'-*-'.join(parts)}")

# function6()

def function7():
    # strings
    str1, str2 = "python", "programming"
    scheme, domain, path, query_string = "https", "google.com", "search", "q=python"

    # string concatenation
    print(f"{str1} + {str2}       = {str1 + str2}")
    print(f"{str1} + ' ' + {str2} = {str1 + ' ' + str2}")
    print(f'-' * 80)

    # string concatenation
    url = scheme + "://" + domain + "/" + path + '?' + query_string
    print(f"url = {url}")

    # string interpolation
    url = f"{scheme}://{domain}/{path}?{query_string}"
    print(f"url = {url}")
    print(f'-' * 80)

    # string repeatition
    print(f"'+' * 10 = {'+' * 10}")
    print(f"'|-' * 10 = {'|-' * 10}")

# function7()

def function8():
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

    # print the data
    # for car in cars:
    #     print(f"{car['model']} | {car['brand']} | {car['price']} | {car['fuel_type']} | {car['transmission']}")


    # print the formatted data
    print('-' * 77)
    print(f"| {'model':<15} | {'brand':<15} | {'price':>8} | {'fuel_type':<10} | {'transmission':<13} |")
    print('-' * 77)
    for car in cars:
        print(f"| {car['model']:<15} | {car['brand']:<15} | {car['price']:>8} | {car['fuel_type']:<10} | {car['transmission']:<13} |")
    print('-' * 77)

function8()
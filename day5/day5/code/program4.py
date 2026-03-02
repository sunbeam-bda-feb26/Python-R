# dictionary
# - a mutable collection of key-value pairs
# - for every value there must a key associated with it
# - key
#   - used to find a value uniquely
#   - keys must be unique
#   - key can be of different type: string, number, boolean
#     - but only strings are encouraged
#   - keys can not be a type of a collection: list, set, dict are not allowed as keys
# - value
#   - can be of any type
#   - can be duplicate as well
# - methods
#   - get(): get value of a key
#   - items(): returns all key-value pairs in the form of List of Tuples

def function1():
    # list of numbers
    numbers_list = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50] 
    print(f"numbers_list         = {numbers_list}, type = {type(numbers_list)}")

    # tuple of numbers
    numbers_tuple = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
    print(f"numbers_tuple        = {numbers_tuple}, type = {type(numbers_tuple)}")

    # mutable set of numbers
    numbers_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(f"numbers_set          = {numbers_set}, type = {type(numbers_set)}")

    # immutable set of numbers
    numbers_frozen_set = frozenset([10, 20, 30, 40, 50, 10, 20, 30, 40, 50])
    print(f"numbers_frozen_set   = {numbers_frozen_set}, type = {type(numbers_frozen_set)}")

    # dictionary of numbers
    numbers_dict = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50, 5: 10, 6: 20, 7: 30, 8: 40, 9: 50}
    print(f"numbers_dict         = {numbers_dict}, type = {type(numbers_dict)}")

# function1()


def function2():
    # dictionary representing a persons information
    person = {
        # value: string
        "first_name": "john",
        "last_name": "doe",
        "email": "john@test.com",

        # value: int
        "age": 30,

        # value: float
        "salary": 25.50,

        # value: list
        "hobbies": ["reading", "playing", "watching movies"],

        # value: dictionary
        "address": {
            "city": "pune",
            "state": "maharashtra",
            "zipcode": 411041
        }
    }

    # get all keys
    print(f"keys    = {person.keys()}")
    
    # get all values
    print(f"values  = {person.values()}")

# function2()

def function3():
    # dictionary representing a persons information
    person = {
        "first_name": "john",
        "last_name": "doe",
        "email": "john@test.com",
        "age": 30,
        "salary": 25.50,
        "company": "sunbeam"
    }

    # read all the values from person dictionary
    print(f"first name = {person['first_name']}")
    print(f"last name  = {person['last_name']}")
    print(f"email      = {person['email']}")
    print(f"age        = {person['age']}")
    print(f"salary     = {person['salary']}")

    # trying to access the key which does NOT exist in the dictionary
    # raises an exception - KeyError: 'address'
    # print(f"address    = {person['address']}")
    print(f"-" * 80)

    # read all the values from person dictionary
    print(f"first name = {person.get('first_name')}")
    print(f"last name  = {person.get('last_name')}")
    print(f"email      = {person.get('email')}")
    print(f"age        = {person.get('age')}")
    print(f"salary     = {person.get('salary')}")
    
    # trying to access the key which does NOT exist in the dictionary
    # get() returns None if the key does not exist
    # it does NOT raise any exception
    print(f"address    = {person.get('address')}")
    print(f"-" * 80)

    # get all key-value pairs
    for key in person:
        # get the value by using the key
        print(f"key = {key}, value = {person[key]}")
    print(f"-" * 80)
    
    # get all key-value pairs in the form of list of tuples
    # print(f"items = {person.items()}")
    # for item in person.items():
    #     # print(f"item = {item}")
    #     print(f"key = {item[0]}, value = {item[1]}")

    # get all key-value pairs in the form of list of tuples
    # for item in person.items():
    #     # tuple unpacking
    #     key, value = item
    #     print(f"key = {key}, value = {value}")

    # tuple unpacking while reading all the items
    # for (key, value) in person.items():
    for key, value in person.items():
        print(f"key = {key}, value = {value}")
        
# function3()


def function4():
    # dictionary representing a persons information
    person = {
        "first_name": "john",
        "last_name": "doe",

        # repeat a key with different value
        "first_name": "jane"
    }

    # since the first_name is repeated, the last one will
    # overwrite the first one and finally the value 'Jane' will be stored
    # person = {'first_name': 'jane', 'last_name': 'doe'}
    print(f"person = {person}")

# function4()

def function5():
    # dictionary representing a persons information
    person = {
        "first_name": "john",
        "last_name": "doe",
        "company": "sunbeam"
    }
    print(f"person = {person}")

    # add a new key-value pair dynamically
    # if the key is NOT present, a pair gets added as a new item
    person['email'] = 'john@test.com'
    print(f"person = {person}")

    # change the value of existing key
    # if the key already exists, the value gets updated
    person['company'] = 'microsoft'
    print(f"person = {person}")

# function5()

def function6():
    # dictionary representing a persons information
    person = {
        "first_name": "john",
        "last_name": "doe",
        "email": "john@test.com",
        "age": 30,
        "salary": 25.50,
        "company": "sunbeam"
    }
    print(f"person = {person}")

    # delete existing key-value pair dynamically
    # can be done by deleting the key
    # when a key gets deleted, the value associated with it also gets removed
    del person['salary']
    del person['company']
    print(f"person = {person}")

# function6()

def function7():
    # string
    string = "My name is Amit. I stay in pune. I work for Sunbeam. I am also a freelancer."
    print(f"string = {string}")

    # find the characters and their count in the string

    # convert all the characters to the lower case
    string = string.lower()
    print(f"string = {string}")

    # start with en empty dictionary
    # which will store the character and its count
    # key: character, value: count
    dictionary_count = {}

    # iterate over the string to get every character
    for ch in string:
        # check if the character is already present in the dictionary
        if ch in dictionary_count.keys():
            # character is found, increment its count
            dictionary_count[ch] += 1
        else:
            # character is not yet found in the dictionary
            # set the count to 1
            dictionary_count[ch] = 1
        
    print(dictionary_count)

function7()


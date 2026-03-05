from flask import Flask, request
import json

# create a flask application
app = Flask(__name__)

# create a collection to store the data
with open("persons.json", "r") as file:
    persons = json.load(file)

def persist_data():
    # persist the collection to the json file
    with open("persons.json", "w") as file:
            json.dump(persons, file)

# get all the persons
@app.route('/person', methods=['GET'])
def get_persons():
    # return all the persons in list of dictionaries format
    return persons

# insert the person information in the collection
@app.route('/person', methods=['POST'])
def create_person():
    name = request.json['name']
    address = request.json['address']
    age = request.json['age']
    email = request.json['email']

    # add the new data to the collection
    persons.append({
        "name": name, 
        "address": address, 
        "age": age,
        "email": email
    })

    # persist the collection to the json file
    persist_data()

    return "added new person"

# update the person information in the collection
@app.route('/person', methods=['PUT'])
def update_person():
    old_email = request.json['old_email']
    name = request.json['name']
    address = request.json['address']
    age = request.json['age']
    email = request.json['email']

    # find the person by email
    for person in persons:
        if person['email'] == old_email:
            person['name'] = name
            person['address'] = address
            person['email'] = email
            person['age'] = age

            # persist the data
            persist_data()

            return "updated person information"
        
    return "person does not exist"

# delete the person information 
@app.route('/person/<email>', methods=['DELETE'])
def delete_person(email):
    print(f"email = {email}")
    
    # find the person by email
    for index in range(len(persons)):
        person = persons[index]
        if person['email'] == email:

            # delete the persons data
            persons.pop(index)
            
            # persist the data
            persist_data()

            return "deleted person information"
        
    return "person does not exist"

# run the application
app.run(host="0.0.0.0", port=5600, debug=True)

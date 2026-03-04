import json

# maintain the list of persons
persons = []

# read the previous contents
with open("persons.json", "r") as file:
    persons = json.load(file)

def read_person_information():
    name = input("enter your name      : ")
    address = input("enter your address: ")
    age = int(input("enter your age       :"))
    email = input("enter your email      :")

    # append the person information to the list
    persons.append({
        "name": name, "address": address, "age": age, "email": email
    })

    # save the contents of list to a file
    with open("persons.json", "w") as file:
        json.dump(persons, file)
    
def print_all_persons():
    print('-' * 64)
    print(f"| {'name':<15} | {'address':<15} | {'age':>8} | {'email':<10} |")
    print('-' * 64)
    for person in persons:
        print(f"| {person['name']:<15} | {person['address']:<15} | {person['age']:>8} | {person['email']:<10} |")
    print('-' * 64)

def search_person_by_email():
    email = input("enter email to search: ")
    for person in persons:
        if person['email'] == email:
            print(f"| {person['name']:<15} | {person['address']:<15} | {person['age']:>8} | {person['email']:<10} |")
            return
    print("person does not exist")

def delete_person_by_email():
    email = input("enter email to search: ")
    for index in range(len(persons)):
        # read the person info from persons collection
        person = persons[index]

        # find the person by email
        if person['email'] == email:
            # found the person, now remove the persons information
            persons.pop(index)

            # save the contents of list to a file
            with open("persons.json", "w") as file:
                json.dump(persons, file)

            return

    print("person does not exist")


def print_menu_and_get_choice():
    print(f'-' * 80)
    print(f"welcome to my JOSN demo application")
    print(f"1. add a person information")
    print(f"2. print list of persons")
    print(f"3. search a person by email")
    print(f"4. delete a person by email")
    print(f"q: exit")
    print(f'-' * 80)
    choice = input("enter your choice: ")
    return choice

# menu driven application

# infinite while loop: this loop will never break on its own
while True:
    # print the menu and get the choice from user
    choice = print_menu_and_get_choice()

    if choice == '1':
        read_person_information()
    elif choice == '2':
        print_all_persons()
    elif choice == '3':
        search_person_by_email()
    elif choice == '4':
        delete_person_by_email()
    elif choice == 'q':
        break
    else:
        print(f"invalid option selected.")

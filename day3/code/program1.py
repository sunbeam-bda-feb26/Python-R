# this is NOT the right way to write the code
# - this code is duplicating the code multiple times
# - it becomes difficult to modify the code

# person1's age
person1_age = 23
if person1_age >= 18:
    print("person is eligible for voting")
else:
    print("person is NOT eligible for voting")

# person2's age
person2_age = 10
if person2_age >= 18:
    print("person is eligible for voting")
else:
    print("person is NOT eligible for voting")

# person3's age
person3_age = 56
if person3_age >= 18:
    print("person is eligible for voting")
else:
    print("person is NOT eligible for voting")

print('-' * 80)

# this is a right way to implement the logic

def can_vote(age: int):
    if age >= 18:
        print("person is eligible for voting")
    else:
        print("person is NOT eligible for voting")

# call the function
can_vote(person1_age)
can_vote(person2_age)
can_vote(person3_age)
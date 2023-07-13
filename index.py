

database = [
    {'name': 'KArina ', 'age': 23, 'hobby': 'sleep', 'StatusAge': 'You are adult'}, 
    {'name': 'SHerzod', 'age': 203, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 18, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 44, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 23, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 17, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 23, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 15, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'SHerzod', 'age': 55, 'hobby': 'boxing', 'StatusAge': 'you are not alive'}, 
    {'name': 'Diyor', 'age': 15, 'hobby': 'girls', 'StatusAge': 'Go to school'}
    ]

# for i in range (3): 
#     person_name = str(input("Enter your name: "))
#     person_age = int(input("Enter your age: "))
#     person_hobby = str(input("Enter your hobby: "))


#     Person = {
#         "name": person_name,
#         "age": person_age,
#         "hobby": person_hobby
#     }

#     if person_age < 0:  
#         Person["StatusAge"] = "Person does not exist"
#     elif 0 < person_age <= 18:
#         Person["StatusAge"] = "Go to school"
#     elif 19 < person_age < 150:
#         Person["StatusAge"] = "You are adult"
#     else:
#         Person["StatusAge"] = "you are not alive"

#     database.append(Person)
    
# print(database)

age_list = []
for Person in database:
    print(Person["age"])
    age_list.append(Person["age"])

print(age_list)

print(sorted(age_list))
print(sorted(set(age_list)))



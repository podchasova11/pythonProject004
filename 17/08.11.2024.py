users = [
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 200
    },
    {
        "firstName": "Margo",
        "lastName": "Rose",
        "gender": "male",
        "salary": 150
    },
    {
        "firstName": "Lisa",
        "lastName": "Barcley",
        "gender": "male",
        "salary": 1600
    },
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 2600
    },
]

print("Полные имена:")
for user in users:
    full_name = f"{user['firstName']} {user['lastName']}"
    print(full_name)

total_salary = sum(user['salary'] for user in users)
print("\nИтоговая зарплата:", total_salary)

print("\nИмена с фамилией 'Rose':\n")
roses = [user['firstName'] for user in users if user['firstName'] == 'Rose']
for name in roses:
    print(name)

unique_last_names = {user['lastName'] for user in users}
print("\nКоличество уникальных фамилий:", len(unique_last_names))


name = (user["firstName"] for user in users if user["lastName"] == "Rose")
for n in name:
    print(n)

name = [user["firstName"] for user in users if user["lastName"] == "Rose"]
for a in name:
    print(a)

gender = [name["gender"] for name in users if name["salary"] == 150]
for i in gender:
    print(i)
    

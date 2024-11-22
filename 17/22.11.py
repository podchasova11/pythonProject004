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
# total_salary = 0
# print(f'Полные имена:')
# for user in users:
#     print(f'{user["firstName"]} {user["lastName"]}')
#
# for user in users:
#
#
#     total_salary += user["salary"]
#     a = total_salary
#     print(a)

users = [
    {
     "name": "Alice",
     "salary": 50000
    },

    {
        "name": "Bob",
        "salary": 60000
    },

    {"name": "Charlie",
     "salary": 55000},
]

# Инициализация переменной для хранения суммы
total_salary = 0

# Перебор каждого пользователя в списке users
for user in users:
    # Добавление зарплаты текущего пользователя к общей сумме
    total_salary += user["salary"]

# Присваивание результата переменной a
a = total_salary

# Вывод суммы
print(a)  # Вывод: 165000

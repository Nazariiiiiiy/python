name = input("Впиши своє ім'я: ")
age = input("Скільки вам повних років: ")

if not name:
    name = "Anonymous"
    print(f"Ім'я не було введено, ви {name}.")

if not age:
    print("Вік не було введено.")
else:
    age = float(age)

    if age != int(age):
        print("Вік повинен бути цілим числом.")
    else:
        age = int(age)

        if age < 0:
            category = "invalid age"
        elif age <= 6:
            category = "child"
        elif age <= 17:
            category = "schoolchild"
        elif age <= 64:
            category = "adult"
        else:
            category = "senior"

        print(f"Привіт, {name}! Ваша вікова категорія: {category}.")
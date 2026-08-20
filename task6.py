name = input("Введіть  ім'я: ")
age = int(input("Введіть  вік: "))
in_range = 18 <= age <= 60
even = age % 2 == 0
both = in_range and even
one = in_range or even
left = 60 - age

print("Ім'я:", name)
print("Вік від 18 до 60:", in_range)
print("Вік парний:", even)
print("Обидві умови виконуються:", both)
print("Хоча б одна умова виконується:", one)
print("До 60 років залишилось:", left)
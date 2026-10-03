full_name = "MIschuk nazariy Yurovych "
full_name = " ".join(full_name.split()).title()
print(full_name, len(full_name))

surname, name, patronymic = full_name.split()
print(surname[0], surname[-1])
print(surname[::-1])
print(surname[0] + name[0] + patronymic[0])
print(f"{surname} {name[0]}. {patronymic[0]}.")

count = 0 
for ch in full_name.lower():
    if ch in "aeiouy":
        count += 1
print(count)

group = "IT-32"
i = group.find("-")
left = group[:i]
right = group[i+1:]
print(left, right, right.isdigit())

login = f"{name[0].lower()}.{surname.lower()}"
print(login)
print(f"{login}@fktpb.net.ua")
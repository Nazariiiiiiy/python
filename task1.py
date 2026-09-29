name = "Nazar"
surname = "Mischuck"
group = "IT-32"

me = {
    "name": name,
    "surname": surname,
    "group": group,
    "city": "Rovantsi",
    "birth_year": 2009,
    "hobbies": ["dance", "gaming", "walking"],
}

for key, value in me.items():
    print(key, ":", value)

print("Keys:", list(me.keys()))
print("Pairs:", len(me))

print("Group:", me["group"])
print("Email:", me.get("email", "unknown"))


me["email"] = "nazar.mischuck@student.edu.ua"
me["city"] = "Lutsk"
removed = me.pop("birth_year")
print("Removed birth_year:", removed)
print(me)

print("Has phone:", "phone" in me)
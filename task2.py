NAME = "Nazariy"
SURNAME = "Mischuk"
GROUP = "IT-32"
Y = 2009


def print_age(year):
    print(f"Age: {2026 - year}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    age = current_year - year
    return age
    print("after return")


print(f"{NAME} {SURNAME}, {GROUP}")

result = print_age(Y)
print(f"print_age returned: {result}")

age = get_age(Y)
print(f"Age from get_age: {age}")
print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")

age_2030 = get_age(Y, current_year=2030)
print(f"Age in 2030: {age_2030}")

try:
    result2 = print_age(Y) * 12
except TypeError as e:
    print("Error:", e)

invalid = get_age(3000)
print(f"Invalid year 3000 gives: {invalid}")
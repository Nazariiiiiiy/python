NAME = "Nazariy"
SURNAME = "Mischuk"
GROUP = "IT-32"
YEAR = 2009


def print_card():
    print(f"Name: {NAME} {SURNAME}")
    print(f"Group: {GROUP}")
    print(f"Birth year: {YEAR}")


def print_card_args(name, surname, year, group=GROUP):
    print(f"{name} {surname}, {group}, {year}")


print(f"{NAME} {SURNAME}, {GROUP}")

for i in range(1, 4):
    print(f"--- no parameters, call {i} ---")
    print_card()

print("--- positional arguments ---")
print_card_args(NAME, SURNAME, YEAR, GROUP)

print("--- keyword arguments ---")
print_card_args(year=YEAR, group=GROUP, surname=SURNAME, name=NAME)

print("--- mixed arguments ---")
print_card_args(NAME, SURNAME, year=YEAR)

print("--- default group ---")
print_card_args(NAME, SURNAME, YEAR)

print("--- calling print_card_args('Nazariy') ---")
try:
    print_card_args("Nazariy")
except TypeError as e:
    print("Error:", e)

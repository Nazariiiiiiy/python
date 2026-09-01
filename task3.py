NAME = "Nazariy"
SURNAME = "Mischuk"
GROUP = "IT-32"


def get_initials(name: str, surname: str) -> str:
    return f"{name[0]}.{surname[0]}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0
    for ch in text:
        if ch.lower() == letter.lower():
            count += 1
    return count


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def reverse_text(text: str) -> str:
    result = ""
    for ch in text:
        result = ch + result
    return result


print(f"{NAME} {SURNAME}, {GROUP}")
print(f"Initials: {get_initials(NAME, SURNAME)}")

c = len(SURNAME)
vowels = count_vowels(SURNAME)
consonants = c - vowels
print(f"Letters in surname: {c}")
print(f"Vowels: {vowels}, consonants: {consonants}")

for v in "aeiou":
    print(f"{v}: {count_letters(SURNAME, letter=v)}")

print(f"Default letter 'a': {count_letters(SURNAME)}")
print(f"Reversed surname: {reverse_text(SURNAME)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")
name = "Nazar"
surname = "Mischuk"
group = "IT-32"

print(f"{name} {surname}, {group}")

full_name = name + surname
vowels_letters = "aeiouyAEIOUY"   # усі голосні у двох регістрах

vowels_count = 0
consonants_count = 0

for letter in full_name:
    if letter in vowels_letters:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {len(full_name)}")
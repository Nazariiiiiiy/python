surname = "Mischuck"

letters = list(surname.lower())  
c = len(letters)
print("1) Список літер прізвища:", letters)
print("   Довжина (c):", c)
print()

first = letters[0]
middle = letters[c // 2]           
last_v1 = letters[-1]              
last_v2 = letters[len(letters) - 1]  
print("2) Перша літера:", first)
print("   Середня літера:", middle)
print("   Остання літера (спосіб 1, letters[-1]):", last_v1)
print("   Остання літера (спосіб 2, letters[len-1]):", last_v2)
print()

first_three = letters[:3]              
without_first_three = letters[3:]      
every_second = letters[::2]            
reversed_letters = letters[::-1]       
last_two = letters[-2:]               
slice_from_c = letters[c:c + 5]       



print("3) Перші три літери:", first_three)
print("   Усе, крім перших трьох:", without_first_three)
print("   Кожна друга літера:", every_second)
print("   У зворотному порядку:", reversed_letters)
print("   Останні дві літери:", last_two)
print(f"   Зріз довжиною 5, що починається з позиції {c}:", slice_from_c)
print()

unique = []
for letter in letters:
    if letter not in unique:
        unique.append(letter)
print("4) Унікальні літери (у порядку першої появи):", unique)

has_repeats = False
for letter in unique:
    count = letters.count(letter)
    if count > 1:
        print(f"   Літера '{letter}' повторюється {count} раз(и)")
        has_repeats = True

if not has_repeats:
    print("   No repeated letters")
print()

alphabetical = sorted(letters)
print("5) Літери прізвища в алфавітному порядку:", alphabetical)
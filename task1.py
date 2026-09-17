name = "Nazar"
surname = "Mischuck"
group = "IT-32"
c = len(surname) 

print(f"{name} {surname}, {group}")
print(f"c (кількість літер у прізвищі) = {c}")
print()

grades = [10, 8, 12, 7, 9, 11, 6, 10]

print("1) Список оцінок:", grades)
print("   Кількість оцінок:", len(grades))
print("   Сума оцінок:", sum(grades))
print("   Найкраща оцінка:", max(grades))
print("   Найгірша оцінка:", min(grades))
print("   Середнє арифметичне:", round(sum(grades) / len(grades), 2))
print()


grades_sorted_desc = sorted(grades, reverse=True)  
print("2) Оцінки від найкращої до найгіршої (новий список):", grades_sorted_desc)
print("   Оригінальний список grades (не змінився):", grades)
print()

top3_best = grades_sorted_desc[:3]         
top3_worst = sorted(grades)[:3]             
print("3) Три найкращі оцінки:", top3_best)
print("   Три найгірші оцінки:", top3_worst)
print()

worst_grade = min(grades)
worst_position = grades.index(worst_grade) + 1  
print(f"4) Найгірша оцінка ({worst_grade}) стоїть на позиції №{worst_position} у списку")
print()

average = sum(grades) / len(grades)
above_average = [g for g in grades if g > average]
print("5) Оцінки вищі за середнє:", above_average)
print("   Їх кількість:", len(above_average))
print()

print("6) Чи є оцінка 12 у списку?", 12 in grades)
print("   Чи є оцінка 1 у списку?", 1 in grades)
print()

print("7) Зміни списку:")

new_value = c % 12 + 1  
grades.append(new_value)
print(f"   Додали в кінець {new_value}:", grades)

grades.insert(0, 12)
print("   Вставили 12 на початок:", grades)

grades.remove(min(grades))
print("   Вилучили найгіршу оцінку:", grades)

removed_last = grades.pop()
print(f"   Вилучили останній елемент (це було {removed_last}):", grades)
print()

count_12 = grades.count(12)
print(f"8) Оцінка 12 трапляється у списку {count_12} раз(и)")
print()

result = grades.sort()
print("9) Список після сортування на місці:", grades)
print("   Значення, яке повернула grades.sort():", result)
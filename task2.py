grades_str = "12, 12, 12, 12, 12"
grades = [int(x) for x in grades_str.split(", ")]  

print(f"{sum(grades) / len(grades):.2f}")   
print(max(grades), min(grades))

print(" | ".join(str(g) for g in grades))  

subjects_str = "Programming, Math, English, Physics, History"
subjects = subjects_str.split(", ")

print(f"{'№':<3}{'Предмет':<15}{'Оцінка':>6}")
for i in range(len(subjects)):
    print(f"{i+1:<3}{subjects[i]:<15}{grades[i]:>6}")

longest = max(subjects, key=len)       
print(longest, len(longest))
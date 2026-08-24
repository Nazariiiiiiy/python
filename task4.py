score = int(input("Введіть бал"))
missed = int(input("Внести дані про пропущені заняття"))

if score < 0 or score > 100:
    print("Недійсний бал")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 4.8:
        print("Недопуск")
    
    if score >= 60 and missed <= 4.8:
        result = "Складено"
    else:
        result = "Не складено"

    print(f"Бали: {score}, Оцінка: {grade}, Result: {result}")
NAME = "Nazariy"
SURNAME = "Mischuk"
GROUP = "IT-32"
N = 7  


def read_grade(prompt):
    """Запитує ціле число від 0 до 100, доки не введуть коректне."""
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Error: digits only")
            continue
        grade = int(value)
        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue
        return grade


def to_letter(grade):
    """Повертає буквену оцінку A-F за числовою оцінкою."""
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    if grade >= 50:
        return "E"
    return "F"


def average(grades):
    """Повертає середнє арифметичне списку оцінок."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Повертає кількість оцінок, більших за limit."""
    count = 0
    for g in grades:
        if g > limit:
            count += 1
    return count


def print_report(name, surname, group, grades):
    """Друкує звіт: оцінки, середнє, найкращий і найгірший бал."""
    avg = average(grades)
    letter = to_letter(avg)
    print("--- Report ---")
    print(f"Student: {name} {surname}, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, avg)}")


def main():
    """Керує програмою: збирає оцінки та друкує звіт."""
    grades = []
    for i in range(N):
        grade = read_grade(f"Grade {i + 1} (0-100): ")
        grades.append(grade)
    print_report(NAME, SURNAME, GROUP, grades)


main()
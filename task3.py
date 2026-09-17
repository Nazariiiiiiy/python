def print_header():
    """Виводить ім'я, прізвище та групу."""
    print("Nazar Mischuck, IT-32")


def print_subjects_table(subjects):
    """Виводить таблицю предметів з нумерацією від 1."""
    print(f"{'#':<3}{'Subject':<15}{'Pairs':>6}{'Grade':>7}")
    for i, (title, pairs, grade) in enumerate(subjects, start=1):
        print(f"{i:<3}{title:<15}{pairs:>6}{grade:>7}")


def total_pairs(subjects):
    """Повертає суму пар на тиждень з усіх предметів."""
    return sum(pairs for (title, pairs, grade) in subjects)


def subject_with_most_pairs(subjects):
    """Повертає кортеж предмета з найбільшою кількістю пар на тиждень."""
    return max(subjects, key=lambda s: s[1])  # s[1] - це pairs


def subject_with_lowest_grade(subjects):
    """Повертає кортеж предмета з найнижчою оцінкою."""
    return min(subjects, key=lambda s: s[2])  # s[2] - це grade


def get_titles(subjects):
    """Повертає окремий список назв предметів."""
    return [title for (title, pairs, grade) in subjects]


def get_grades(subjects):
    """Повертає окремий список оцінок."""
    return [grade for (title, pairs, grade) in subjects]


def titles_with_high_grade(subjects, threshold=10):
    """Повертає назви предметів з оцінкою threshold і вище."""
    return [title for (title, pairs, grade) in subjects if grade >= threshold]


def print_histograms(subjects):
    """Для кожного предмета виводить рядок '#' довжиною = оцінка."""
    for title, pairs, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake_lowest(subjects):
    """
    Знаходить предмет з найнижчою оцінкою, піднімає оцінку на 2 бали
    (але не більше 12) і повертає НОВИЙ список кортежів
    (кортежі незмінні, тому старий кортеж не можна поправити "на місці" -
    його потрібно замінити новим).
    """
    weakest = subject_with_lowest_grade(subjects)
    weakest_title, weakest_pairs, weakest_grade = weakest
    new_grade = min(weakest_grade + 2, 12)

    updated_subjects = []
    for subj in subjects:
        if subj == weakest:
            updated_subjects.append((weakest_title, weakest_pairs, new_grade))
        else:
            updated_subjects.append(subj)

    print(f"Retake: {weakest_title} {weakest_grade} -> {new_grade}")
    return updated_subjects


def main():
    print_header()

    subjects = [
        ("Programming", 3, 11),
        ("Webrozrobka", 2, 9),
        ("Databases", 2, 10),
        ("Math", 1, 10),
        ("English", 2, 12),
    ]

    print_subjects_table(subjects)

    print("Pairs per week:", total_pairs(subjects))

    most = subject_with_most_pairs(subjects)
    print(f"Most pairs: {most[0]} ({most[1]})")

    weakest = subject_with_lowest_grade(subjects)
    print(f"Weakest subject: {weakest[0]} ({weakest[2]})")

    titles = get_titles(subjects)
    grades = get_grades(subjects)
    average = round(sum(grades) / len(grades), 2)
    print("Titles:", titles)
    print(f"Grades: {grades}, average: {average}")

    print("Grade 10+:", titles_with_high_grade(subjects, 10))

    print_histograms(subjects)

    subjects = retake_lowest(subjects)
    print("Subjects:", subjects)


if __name__ == "__main__":
    main()
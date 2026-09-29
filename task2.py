
schedule = {
    "Mon": ["Administration", "Programming", "Ukr lang"],
    "Tue": ["Databases", "Programming", "IT law"],
    "Wed": ["Web rozrobka", "English", "Web rozrobka"],
    "Thu": ["Administration", "Programming", "Web rozrobka"],
    "Fri": ["IT law", "English", "Databases"],
}

def count_subjects(schedule):
    counts = {}
    for subjects in schedule.values():
        for subject in subjects:
            counts[subject] = counts.get(subject, 0) + 1
    return counts

print("Day  Pairs  Subjects")
total = 0
for day, subjects in schedule.items():
    print(f"{day:<5}{len(subjects):<7}{', '.join(subjects)}")
    total += len(subjects)

print("Pairs per week:", total)


busiest = max(schedule, key=lambda day: len(schedule[day]))
print("Busiest day:", busiest, len(schedule[busiest]))

all_subjects = set()
for subjects in schedule.values():
    all_subjects.update(subjects)
print("Different subjects:", all_subjects, len(all_subjects))

mon = set(schedule["Mon"])
wed = set(schedule["Wed"])
print("Mon and Wed:", mon & wed)
print("Mon but not Wed:", mon - wed)

counts = count_subjects(schedule)
print("Counts:", counts)
ranking = sorted(counts.items(), key=lambda item: item[1], reverse=True)
for i, (subject, count) in enumerate(ranking, 1):
    print(f"{i}. {subject} - {count}")
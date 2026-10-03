import sys
from pathlib import Path

NAME = "Nazar Mischuk"
GROUP = "IT-32"

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "expenses.csv"
REPORT = BASE / "reports" / "expenses_report.txt"

USAGE = """usage: python3 task3.py add <date> <category> <amount> <note>
       python3 task3.py list
       python3 task3.py report"""


def fail(message):
    print("error:", message)
    print(USAGE)


def add_expense(args):
    if len(args) < 4:
        fail("add needs date, category, amount and note")
        return
    date, category = args[0], args[1]
    try:
        amount = float(args[2])
    except ValueError:
        fail("amount must be a number")
        return
    note = " ".join(args[3:])              # склеюємо всі слова опису

    DATA.parent.mkdir(exist_ok=True)
    if not DATA.exists():                  # перший запуск: пишемо заголовок
        DATA.write_text("# date;category;amount;note\n", encoding="utf-8")

    with DATA.open("a", encoding="utf-8") as f:
        f.write(f"{date};{category};{amount:.2f};{note}\n")
    print(f"added: {date} {category} {amount:.2f} ({note})")


def read_expenses():
    records = []
    if not DATA.exists():
        return records
    for line in DATA.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):    # пропускаємо порожні й коментарі
            continue
        date, category, amount, note = line.split(";", 3)
        records.append((date, category, float(amount), note))
    return records


def list_expenses():
    records = read_expenses()
    print(f"{'date':<12}{'category':<12}{'amount':>9}  note")
    total = 0
    for date, category, amount, note in records:
        print(f"{date:<12}{category:<12}{amount:>9.2f}  {note}")
        total += amount
    print(f"{len(records)} records, total {total:.2f}")


def report():
    records = read_expenses()
    if not records:
        print("no expenses yet")
        return

    total = sum(r[2] for r in records)
    dates = sorted(set(r[0] for r in records))

    # рахуємо за категоріями і за днями
    counts, sums, days = {}, {}, {}
    for date, category, amount, note in records:
        counts[category] = counts.get(category, 0) + 1
        sums[category] = sums.get(category, 0) + amount
        days[date] = days.get(date, 0) + amount

    lines = []
    lines.append(f"Expenses report for {NAME} ({GROUP})")
    lines.append(f"Period: {dates[0]} .. {dates[-1]}")
    lines.append(f"Records: {len(records)}")
    lines.append("")
    lines.append(f"{'category':<12}{'count':>5}{'total':>10}{'share':>8}  chart")
    lines.append("-" * 52)

    # сортуємо категорії за сумою від більшої до меншої
    for category, s in sorted(sums.items(), key=lambda item: item[1], reverse=True):
        share = s / total * 100
        chart = "#" * round(share / 5)             # 1 символ = 5 %
        lines.append(f"{category:<12}{counts[category]:>5}{s:>10.2f}{share:>7.1f}%  {chart}")

    lines.append("-" * 52)
    lines.append(f"{'total':<12}{len(records):>5}{total:>10.2f}{100:>7.1f}%")
    lines.append("")

    top_day = max(days, key=days.get)              # день з найбільшою сумою
    top = max(records, key=lambda r: r[2])         # найдорожча покупка
    lines.append(f"Top day: {top_day} ({days[top_day]:.2f})")
    lines.append(f"Most expensive: {top[1]} {top[2]:.2f} ({top[3]})")
    lines.append(f"Average per day: {total / len(dates):.2f}")

    text = "\n".join(lines)
    print(text)

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(text + "\n", encoding="utf-8")
    print()
    print("report saved to: reports/expenses_report.txt")


def main():
    args = sys.argv[1:]          # те, що ви написали після task3.py
    if not args:
        print(USAGE)
        return
    command = args[0]
    if command == "add":
        add_expense(args[1:])
    elif command == "list":
        list_expenses()
    elif command == "report":
        report()
    else:
        fail(f"unknown command {command}")


main()
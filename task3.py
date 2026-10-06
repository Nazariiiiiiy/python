import sys
from datetime import datetime

NAME = "Nazariy Mischuk, IT-32"
FILE = "data/expenses.csv"
USAGE = """usage: python3 task3.py add <date> <category> <amount> <note>
       python3 task3.py list
       python3 task3.py report"""


def parse(fields):
    """Єдине місце перевірки: і для читання файлу, і для add."""
    if len(fields) != 4:
        raise ValueError(f"expected 4 fields, got {len(fields)}")
    date, cat, amount, note = [x.strip() for x in fields]
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"bad date '{date}'") from None
    try:
        value = float(amount)
    except ValueError:
        raise ValueError(f"bad amount '{amount}'") from None
    if not value > 0:
        raise ValueError(f"amount must be positive, got {value:.2f}")
    return date, cat, value, note


def load():
    with open(FILE, encoding="utf-8") as f:
        lines = f.read().splitlines()
    records, bad = [], []
    for n, line in enumerate(lines[1:], start=2):  # 1-й рядок — заголовок
        if not line.strip():
            continue
        try:
            records.append(parse(line.split(";")))
        except ValueError as e:
            bad.append((n, str(e)))
    return records, bad


def show_bad(bad):
    if bad:
        print(f"skipped {len(bad)} bad line(s):", file=sys.stderr)
        for n, why in bad:
            print(f"  line {n}: {why}", file=sys.stderr)


def cmd_add(args):
    try:
        date, cat, value, note = parse(args)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        print("nothing was added", file=sys.stderr)
        return 1
    with open(FILE, encoding="utf-8") as f:  # перевірка, що файл читається
        text = f.read()
    with open(FILE, "a", encoding="utf-8") as f:
        if text and not text.endswith("\n"):
            f.write("\n")
        f.write(f"{date};{cat};{value:.2f};{note}\n")
    print(f"added: {date} {cat} {value:.2f}")
    return 0


def cmd_list():
    records, bad = load()
    print(f"{'date':<12}{'category':<14}{'amount':>8}  note")
    for d, c, v, n in records:
        print(f"{d:<12}{c:<14}{v:>8.2f}  {n}")
    print(f"{len(records)} records, total {sum(r[2] for r in records):.2f}")
    show_bad(bad)
    return 0


def cmd_report():
    records, bad = load()
    if not records:
        print("error: nothing to report, no valid records", file=sys.stderr)
        show_bad(bad)
        return 1
    totals = {}
    for _, c, v, _ in records:
        totals[c] = totals.get(c, 0) + v
    for c, v in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{c:<14}{v:>10.2f}")
    print(f"{'TOTAL':<14}{sum(totals.values()):>10.2f}")
    show_bad(bad)
    return 0


def main():
    print(NAME)
    args = sys.argv[1:]
    if not args:
        print(USAGE, file=sys.stderr)
        return 2
    cmd = args[0]
    if cmd not in ("add", "list", "report"):
        print(f"error: unknown command {cmd}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2
    if (cmd == "add" and len(args) != 5) or (cmd != "add" and len(args) != 1):
        print(USAGE, file=sys.stderr)
        return 2
    try:
        if cmd == "add":
            return cmd_add(args[1:])
        return cmd_list() if cmd == "list" else cmd_report()
    # усі проблеми самого файлу — в одному місці
    except FileNotFoundError:
        print(f"error: {FILE} not found", file=sys.stderr)
    except IsADirectoryError:
        print(f"error: {FILE} is a directory, not a file", file=sys.stderr)
    except PermissionError:
        print(f"error: no permission to access {FILE}", file=sys.stderr)
    except UnicodeDecodeError:
        print(f"error: {FILE} is not a UTF-8 text file", file=sys.stderr)
    except OSError as e:
        print(f"error: {FILE}: {e.strerror}", file=sys.stderr)
    return 1


sys.exit(main())
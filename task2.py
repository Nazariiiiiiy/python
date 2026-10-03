from pathlib import Path
from datetime import datetime

NAME = "Nazar Mischuk"


def count_runs(path):
    if not path.exists():            
        return 0
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():               
            count += 1
    return count


def add_run(path, number):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with path.open("a", encoding="utf-8") as f:   
        f.write(f"{number};{stamp};{NAME}\n")


def show_history(path, last=3):
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            lines.append(line)

    print("runs so far:", len(lines))
    print("last runs:")
    for line in lines[-last:]:                     
        number, stamp, name = line.split(";")
        print(f"  #{number:>2}  {stamp}  {name}")

    first = lines[0].split(";")[1]                
    print("first run was at", first)


def main():
    path = Path(__file__).resolve().parent / "data" / "runs.log"
    path.parent.mkdir(exist_ok=True)

    first_time = not path.exists()
    number = count_runs(path) + 1
    add_run(path, number)

    print(f"Hello, {NAME}! This is run number {number}.")
    if first_time:
        print("File runs.log was just created.")
    show_history(path)


main()
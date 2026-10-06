
import sys

NAME = "Nazariy Mischuk, IT-32"


def inspect(path):
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return False, f"{path}: file not found (FileNotFoundError)"
    except IsADirectoryError:
        return False, f"{path}: is a directory (IsADirectoryError)"
    except PermissionError:
        return False, f"{path}: permission denied (PermissionError)"
    except UnicodeDecodeError:
        return False, f"{path}: not a UTF-8 text file (UnicodeDecodeError)"
    except OSError as e:
        return False, f"{path}: {e.strerror} ({type(e).__name__})"
    if not lines:
        return False, f"{path}: file is empty (ValueError)"
    return True, f"{path}: {len(lines)} lines, first: {lines[0]}"


def main():
    print(NAME)
    paths = sys.argv[1:]
    if not paths:
        print("usage: python3 task1.py <path> [<path> ...]", file=sys.stderr)
        return 2
    failed = 0
    for p in paths:
        ok, msg = inspect(p)
        if ok:
            print("ok:    " + msg)
        else:
            failed += 1
            print("error: " + msg, file=sys.stderr)
    print(f"checked {len(paths)}, failed {failed}")
    return 1 if failed else 0


sys.exit(main())
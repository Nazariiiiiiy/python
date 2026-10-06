import os
import sys

NAME = "Nazariy Mischuk, IT-32"
USAGE = "usage: python3 task2.py [--force] <source> <destination>"


def copy(src, dst, force):
    if not os.path.exists(src):
        return f"source {src} not found"
    if os.path.isdir(src):
        return f"source {src} is a directory, not a file"
    if os.path.isdir(dst):
        return f"destination {dst} is a directory, not a file"
    folder = os.path.dirname(dst) or "."
    if not os.path.isdir(folder):
        return f"destination folder {folder} not found"
    if os.path.exists(dst) and os.path.samefile(src, dst):
        return "source and destination are the same file"
    if os.path.exists(dst) and not force:
        return f"{dst} already exists, use --force to overwrite"
    try:
        with open(src, encoding="utf-8") as f:
            text = f.read()
        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)
    except UnicodeDecodeError:
        return f"source {src} is not a UTF-8 text file"
    except OSError as e:
        return f"{e.strerror} ({type(e).__name__})"
    return None


def main():
    print(NAME)
    args = sys.argv[1:]
    force = "--force" in args
    args = [a for a in args if a != "--force"]
    if len(args) != 2:
        print(USAGE, file=sys.stderr)
        return 2
    err = copy(args[0], args[1], force)
    if err:
        print("error: " + err, file=sys.stderr)
        return 1
    print(f"copied: {args[0]} -> {args[1]}")
    return 0


sys.exit(main())
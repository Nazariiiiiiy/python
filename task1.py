from pathlib import Path

script = Path(__file__).resolve()    
script_dir = script.parent            

print("cwd:       ", Path.cwd())     
print("script:    ", script)
print("script dir:", script_dir)
print("home:      ", Path.home())    


for folder in ["data", "reports", "backups"]:
    (script_dir / folder).mkdir(exist_ok=True)


profile = script_dir / "data" / "profile.txt"
profile.write_text(
    "name: Nazar\n"
    "surname: Mischuk\n"
    "group: IT-32\n"
    "year: 2007\n"
    "language: Python\n",
    encoding="utf-8",
)

print()
print("profile path:", profile.resolve())
print("relative:    ", profile.relative_to(script_dir))
print("name:        ", profile.name)          
print("stem:        ", profile.stem)          
print("suffix:      ", profile.suffix)       
print("parent:      ", profile.parent.name)   
print("size:        ", profile.stat().st_size, "bytes")

print()
print("project tree:")
for folder in sorted(script_dir.iterdir()):
    if folder.is_dir():
        print(f"  {folder.name}/")
        for f in sorted(folder.iterdir()):
            print(f"    {f.name}")
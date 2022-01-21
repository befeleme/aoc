from pathlib import Path

a = Path("input").read_text().strip()

floor = 0
for char in a:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

print(floor)

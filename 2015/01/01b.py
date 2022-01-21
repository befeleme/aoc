from pathlib import Path

a = Path("input").read_text().strip()

floor = 0
for i, char in enumerate(a):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
        if floor == -1:
            print(i+1)
            break

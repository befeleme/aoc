with open("input", "r") as f:
    strings = f.read().splitlines()

print(sum([len(line) - len(eval(f"str('{line[1:-1]}')")) for line in strings]))
print(sum([sum([2 if char in ("'", '"', '\\') else 1 for char in line], 2) - len(line) for line in strings]))

with open("input", "r") as f:
    strings = f.read().splitlines()

total_1 = 0
for line in strings:
    total_1 +=  len(line) - len(eval(f"str('{line[1:-1]}')"))
print(total_1)

total_2 = 0
for line in strings:
    encoded_chars = [2 if char in ("'", '"', '\\') else 1 for char in line]
    # add 2 to the total length -> string quotation marks
    encoded_length = sum(encoded_chars, 2)
    total_2 += encoded_length - len(line)
print(total_2)

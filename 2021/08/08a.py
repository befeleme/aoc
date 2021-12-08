import fileinput
import re


data = [line.strip() for line in fileinput.input()]
valid_lengths = (2, 3, 4, 7)

counter = 0
pattern = r"\| (\w{2,7}) (\w{2,7}) (\w{2,7}) (\w{2,7})"
for line in data:
    res = re.search(pattern, line)
    for r in res.groups():
        if len(r) in valid_lengths:
            counter += 1

print(counter)

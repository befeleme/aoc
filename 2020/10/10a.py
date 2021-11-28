import fileinput
from collections import Counter


contents = [int(line.strip()) for line in fileinput.input()]

# Add outlet and device joltages (0 and max+3 of the list)
contents.extend([0, max(contents) + 3])
contents.sort()
diffs = []
for i in range(len(contents)):
    try:
        diffs.append(contents[i+1] - contents[i])
    except IndexError:
        break

c = Counter(diffs)
print(c[1]*c[3])

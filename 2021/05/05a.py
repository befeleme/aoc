import fileinput
import re


vents_lines_data = [line.strip() for line in fileinput.input()]

d = {}

vents_lines = []
pattern = r"(\d+),(\d+) -> (\d+),(\d+)"
for vents_line in vents_lines_data:
    vl = re.search(pattern, vents_line)
    x1, y1, x2, y2 = vl.groups()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 != x2 and y1 != y2:
        continue
    else:
        if x1 == x2:
            # 5 - 7 => 5, 6, 7
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    val = d.get((x1, i))
                    if val:
                        d[(x1, i)] = val + 1
                    else:
                        d[(x1, i)] = 1
            else:
                for i in range(y2, y1 + 1):
                    val = d.get((x1, i))
                    if val:
                        d[(x1, i)] = val + 1
                    else:
                        d[(x1, i)] = 1
        if y1 == y2:
            if x1 < x2:
                for i in range(x1, x2 + 1):
                    val = d.get((i, y1))
                    if val:
                        d[(i, y1)] = val + 1
                    else:
                        d[(i, y1)] = 1
            else:
                for i in range(x2, x1 + 1):
                    val = d.get((i, y1))
                    if val:
                        d[(i, y1)] = val + 1
                    else:
                        d[(i, y1)] = 1

counter = 0
for k, v in d.items():
    if v >= 2:
        counter += 1
print(counter)



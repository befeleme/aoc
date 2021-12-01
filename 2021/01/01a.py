import fileinput

depths = []
for line in fileinput.input():
    depths.append(int(line.strip()))

increased = 0

for i, depth in enumerate(depths):
    if i == 0:
        continue
    if depth > depths[i-1]:
        increased += 1

print(increased)

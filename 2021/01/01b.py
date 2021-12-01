import fileinput

depths = []
for line in fileinput.input():
    depths.append(int(line.strip()))

increased = 0

sum_prev = depths[0] + depths[1] + depths[2]
for i, depth in enumerate(depths):
    try:
        sum_now = depth + depths[i+1] + depths[i+2]
    except IndexError:
        break
    if i == 0:
        continue
    if sum_now > sum_prev:
        increased += 1
    sum_prev = sum_now

print(increased)

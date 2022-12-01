# run: `python 01.py input`

import fileinput

data = [line.strip() for line in fileinput.input()]

total = []
subtotal = 0
for cal in data:
    if cal == "":
        total.append(subtotal)
        subtotal = 0
    else:
        cal = int(cal)
        subtotal += cal

total.sort(reverse=True)
# 1st part
print(total[0]))
# 2nd part
print(sum(total[:3]))
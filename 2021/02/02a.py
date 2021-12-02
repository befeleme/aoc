import fileinput

directions = []
for line in fileinput.input():
    directions.append(line.strip())

l = 0
d = 0
for dir in directions:
    which, howmuch = dir.split()
    howmuch = int(howmuch)
    if which == "forward":
        l += howmuch
    elif which == "up":
        d -= howmuch
    elif which == "down":
        d += howmuch

print(d*l)

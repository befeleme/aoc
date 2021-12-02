import fileinput

directions = []
for line in fileinput.input():
    directions.append(line.strip())

l = 0
d = 0
a = 0
for dir in directions:
    which, howmuch = dir.split()
    howmuch = int(howmuch)
    if which == "forward":
        l += howmuch
        d += a * howmuch
    elif which == "up":
        a -= howmuch
    elif which == "down":
        a += howmuch

print(d*l)

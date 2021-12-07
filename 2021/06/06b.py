from collections import Counter

d = [4,1,1,1,5,1,3,1,5,3,4,3,3,1,3,3,1,5,3,2,4,4,3,4,1,4,2,2,1,3,5,1,1,3,2,5,1,1,4,2,5,4,3,2,5,3,3,4,5,4,3,5,4,2,5,5,2,2,2,3,5,5,4,2,1,1,5,1,4,3,2,2,1,2,1,5,3,3,3,5,1,5,4,2,2,2,1,4,2,5,2,3,3,2,3,4,4,1,4,4,3,1,1,1,1,1,4,4,5,4,2,5,1,5,4,4,5,2,3,5,4,1,4,5,2,1,1,2,5,4,5,5,1,1,1,1,1,4,5,3,1,3,4,3,3,1,5,4,2,1,4,4,4,1,1,3,1,3,5,3,1,4,5,3,5,1,1,2,2,4,4,1,4,1,3,1,1,3,1,3,3,5,4,2,1,1,2,1,2,3,3,5,4,1,1,2,1,2,5,3,1,5,4,3,1,5,2,3,4,4,3,1,1,1,2,1,1,2,1,5,4,2,2,1,4,3,1,1,1,1,3,1,5,2,4,1,3,2,3,4,3,4,2,1,2,1,2,4,2,1,5,2,2,5,5,1,1,2,3,1,1,1,3,5,1,3,5,1,3,3,2,4,5,5,3,1,4,1,5,2,4,5,5,5,2,4,2,2,5,2,4,1,3,2,1,1,4,4,1,5]
test = [3,4,3,1,2]

fish = Counter(d)


def step(d):
    zer = d.get(0, 0)
    one = d.get(1, 0)
    two = d.get(2, 0)
    thr = d.get(3, 0)
    fou = d.get(4, 0)
    fiv = d.get(5, 0)
    six = d.get(6, 0)
    sev = d.get(7, 0)
    eig = d.get(8, 0)

    d[8] = zer
    d[0] = one
    d[1] = two
    d[2] = thr
    d[3] = fou
    d[4] = fiv
    d[5] = six
    d[6] = sev + zer
    d[7] = eig


for i in range(256):
    step(fish)

print(fish.total())
import fileinput

data = [line.strip() for line in fileinput.input()]


def create_data_matrix(data):
    m = {}
    for i, row in enumerate(data):
        for j, pos in enumerate(data[i]):
            m[(j, i)] = int(pos)
    return m

maxim_x = len(data[0])
maxim_y = len(data)

m = create_data_matrix(data)
offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
risk = 0
for k, v in m.items():
    neighbors = [(k[0] + o[0], k[1] + o[1]) for o in offsets]
    to_compare = []
    for x, y in neighbors:
        if x < 0 or y < 0 or x >= maxim_x or y >= maxim_y:
            continue
        to_compare.append(m[(x, y)])
    if len(list(filter(lambda x: x <= v, to_compare))) == 0:
        risk = risk + 1 + v

print(risk)
starting = [0, 5, 4, 1, 10, 14, 7]
spoken = []


def evaluate():
    matching = []
    number = spoken[-1]
    if spoken.count(number) == 1:
        spoken.append(0)
    else:
        for i, val in enumerate(spoken, start=1):
            if val == number:
                matching.append(i)
        last_two = sorted(matching)[-2:]
        spoken.append(last_two[1] - last_two[0])


spoken.extend(starting)
while True:
    evaluate()
    if len(spoken) == 2020:
        break
print(spoken[-1])

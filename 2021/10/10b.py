import fileinput


def count_score(p):
    score = 0
    for i in p:
        score *= 5
        score += scores[i]
    return score


data = [line.strip() for line in fileinput.input()]

opening = ("[", "(", "{", "<")
closing = ("]", ")", "}", ">")
scores = {
    "]": 2,
    ")": 1,
    "}": 3,
    ">": 4,
}
all_scores = []

for line in data:
    d = []
    for parenthesis in line:
        if parenthesis in opening:
            d.append(parenthesis)
        elif parenthesis in closing:
            last_open = d.pop()
            if opening.index(last_open) != closing.index(parenthesis):
                # corrupted line, stop processing
                break
            else:
                continue
    else:
        p = []
        for parenthesis in reversed(d):
            p.append(closing[opening.index(parenthesis)])
        all_scores.append(count_score(p))

all_scores.sort()
print(all_scores[len(all_scores) // 2])
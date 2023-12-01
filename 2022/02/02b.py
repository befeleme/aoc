import fileinput

data = [line.strip() for line in fileinput.input()]

print(data[:10])

moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}


def find_choice(opponent, result):
    if result == "Y":
        # draw means 3
        return evaluate_choice(opponent) + 3
    elif result == "X":
        if moves[opponent] == "rock":
            return 3
        elif moves[opponent] == "paper":
            return 1
        elif moves[opponent] == "scissors":
            return 2
    else:
        if moves[opponent] == "rock":
            return 8
        elif moves[opponent] == "paper":
            return 9
        elif moves[opponent] == "scissors":
            return 7


def evaluate_choice(b):
    if moves[b] == "rock":
        return 1
    if moves[b] == "paper":
        return 2
    if moves[b] == "scissors":
        return 3

total = 0
for r in data:
    their, res = r.split()
    total += find_choice(their, res)

print(total)
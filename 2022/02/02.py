import fileinput

data = [line.strip() for line in fileinput.input()]

print(data[:10])

moves = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
}

def evaluate_round(a, b):
    if moves[a] == moves[b]:
        return 3
    elif moves[a] == "rock" and moves[b] == "paper" or \
        moves[a] == "paper" and moves[b] == "scissors" or \
        moves[a] == "scissors" and moves[b] == "rock":
        return 6
    else:
        return 0

def evaluate_choice(b):
    if moves[b] == "rock":
        return 1
    if moves[b] == "paper":
        return 2
    if moves[b] == "scissors":
        return 3

total = 0
for r in data:
    their, my = r.split()
    total = total + (evaluate_choice(my) + evaluate_round(their, my))

print(total)
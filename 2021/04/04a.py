import fileinput

bingo = [line.strip().split() for line in fileinput.input()]

draws = bingo.pop(0)
draws = [int(d) for d in draws[0].split(",")]

new_bingo = []
board = []
for board_line in bingo:
    line = []
    if board_line:
        for no in board_line:
            line.append((int(no), 0))
        board.append(line)

    if len(board) == 5:
        new_bingo.append(board)
        board = []


def is_win(bingo):
    # horizontally:
    for i, board in enumerate(bingo):
        for bl in board:
            counter = 0
            for no, hit in bl:
                if hit:
                    counter += 1
            if counter == 5:
                return board
    # vertically
    for board in bingo:
        for i in range(5):
            counter = 0
            for bl in board:
                no, hit = bl[i]
                if hit:
                    counter += 1
                if counter == 5:
                    return board

for draw in draws:
    for k, board in enumerate(new_bingo):
        for i, bl in enumerate(board):
            for j, item in enumerate(bl):
                no, hit = item
                if draw == no:
                    new_bingo[k][i][j] = (no, 1)
    winner = is_win(new_bingo)
    if winner:
        print(winner)
        break

score = 0
for bl in winner:
    for no, hit in bl:
        if not hit:
            score += no

score *= draw
print(score)






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
    winners = []
    # horizontally:
    for i, board in enumerate(bingo):
        for bl in board:
            counter = 0
            for no, hit in bl:
                if hit:
                    counter += 1
            if counter == 5:
                winners.append(board)
    # vertically
    for board in bingo:
        for i in range(5):
            counter = 0
            for bl in board:
                no, hit = bl[i]
                if hit:
                    counter += 1
                if counter == 5:
                    if board not in winners:
                        winners.append(board)
    return winners


winners_aside = []
for draw in draws:
    for k, board in enumerate(new_bingo):
        for i, bl in enumerate(board):
            for j, item in enumerate(bl):
                no, hit = item
                if draw == no:
                    new_bingo[k][i][j] = (no, 1)
    winners = is_win(new_bingo)
    real_winner = ""
    if winners:
        for winner in winners:
            if not winners_aside:
                winners_aside.append(winner)
            else:
                for win in winners_aside:
                    if win == winner:
                        break
                else:
                    winners_aside.append(winner)
            if len(winners_aside) == len(new_bingo):
                real_winner = winner
                break
        if real_winner:
            score = 0
            for bl in winner:
                for no, hit in bl:
                    if not hit:
                        score += no

            score *= draw
            print(score)
            break








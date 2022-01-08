from itertools import cycle

def pos_on_gameboard(pos, throw):
    new_pos = (pos + throw) % 10
    if new_pos == 0:
        new_pos = 10
    return new_pos

def move(player_pos, throw, player_score):
    player_pos = pos_on_gameboard(player_pos, throw)
    player_score += player_pos
    return player_pos, player_score

def deterministic_die():
    for i in cycle(range(1, 101)):
        yield i

die = deterministic_die()

player_1_score = 0
player_2_score = 0

player_1_pos = 6
player_2_pos = 9

throw_counter = 0

while True:
    throw = 0
    for i in range(3):
        throw += next(die)
        throw_counter += 1
    player_1_pos, player_1_score = move(player_1_pos, throw, player_1_score)
    if player_1_score >= 1000:
        print("player 1 wins", player_1_score)
        break
    throw = 0
    for i in range(3):
        throw += next(die)
        throw_counter += 1
    player_2_pos, player_2_score = move(player_2_pos, throw, player_2_score)
    if player_2_score >= 1000:
        print("player 2 wins", player_2_score)
        break

loser = min(player_1_score, player_2_score)
print(loser*throw_counter)

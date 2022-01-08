from itertools import product
from collections import Counter


def pos_on_gameboard(pos, throw):
    new_pos = (pos + throw) % 10
    if new_pos == 0:
        new_pos = 10
    return new_pos


def move(player_pos, throw, player_score):
    player_pos = pos_on_gameboard(player_pos, throw)
    player_score += player_pos
    return player_pos, player_score

# there are 27 possibilities of throwing 1,2,3 dice, each has different frequency
# count them and create freqs dictionary (sum of three throws: count of occurrences)
possible_throws = []
rolls = product([1, 2, 3], repeat=3)
for a, b, c in rolls:
    possible_throws.append(a + b + c)
freqs = Counter(possible_throws)

# game states should be: {(player_1_pos, player_2_pos, player_1_score, player_2_score): count}
game_states = Counter()
# we start with one universe
game_states[(6, 9, 0, 0)] = 1
# initialize victories
victories = {"1": 0, "2": 0}

# game
while game_states:
    new_games = Counter()
    for (player_1_pos, player_2_pos, player_1_score, player_2_score), count in game_states.items():
        for throw, frequency in freqs.items():
            new_player_pos, new_player_score = move(player_1_pos, throw, player_1_score)
            new_count = count * frequency
            if new_player_score >= 21:
                victories["1"] += new_count
            else:
                # Not only assign the new value but first check if the same game state wasn't already processed
                # sum up the extracted count + the new one (that was a tricky mistake not counting with the value already there!)
                new_games[(new_player_pos, player_2_pos, new_player_score, player_2_score)] += new_count

    # update game_states
    game_states = new_games
    new_games = Counter()
    # print(len(game_states), game_states.total())

    for (player_1_pos, player_2_pos, player_1_score, player_2_score), count in game_states.items():
        for throw, frequency in freqs.items():
            new_player_pos, new_player_score = move(player_2_pos, throw, player_2_score)
            new_count = count * frequency
            if new_player_score >= 21:
                victories["2"] += new_count
            else:
                new_games[(player_1_pos, new_player_pos, player_1_score, new_player_score)] += new_count    

    game_states = new_games
    # print(len(game_states), game_states.total())

print(victories)

import fileinput


def play_round():
    print(f"Player 1's deck: {player_1_deck}")
    print(f"Player 2's deck: {player_2_deck}")

    player_1_card = player_1_deck.pop(0)
    player_2_card = player_2_deck.pop(0)
    print(f"Player 1 plays: {player_1_card}")
    print(f"Player 2 plays: {player_2_card}")

    if player_1_card > player_2_card:
        print("Player 1 wins the round!")
        player_1_deck.extend([player_1_card, player_2_card])
    else:
        print("Player 2 wins the round!")
        player_2_deck.extend([player_2_card, player_1_card])


def find_winner():
    if len(player_1_deck) > len(player_2_deck):
        return player_1_deck
    else:
        return player_2_deck


def count_result(deck):
    multiplier = len(deck)
    score = 0
    for card in deck:
        score += card * multiplier
        multiplier -= 1
    return score


if __name__ == "__main__":
    player_1_deck = []
    player_2_deck = []
    for line in fileinput.input():
        if line.startswith("Player 1"):
            current = player_1_deck
            continue
        elif line.startswith("Player 2"):
            current = player_2_deck
            continue
        elif line == "\n":
            continue
        current.append(int(line.strip()))

    counter = 1
    while player_1_deck and player_2_deck:
        print("\n")
        print(f"--- Round {counter} ---")
        play_round()
        counter += 1

    print("\n")
    print("== Post-game results ==")
    print(f"Player 1's deck: {player_1_deck}")
    print(f"Player 2's deck: {player_2_deck}")
    print(f"Score is {count_result(find_winner())}")

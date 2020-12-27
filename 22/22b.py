import fileinput


def play_round(played_decks, player_1_deck, player_2_deck):
    # print(f"Player 1's deck: {player_1_deck}")
    # print(f"Player 2's deck: {player_2_deck}")
    if (player_1_deck, player_2_deck) in played_decks:
        print("Player 1 wins the whole game")
        return 11

    played_decks.append((list(player_1_deck), list(player_2_deck)))
    player_1_card = player_1_deck.pop(0)
    player_2_card = player_2_deck.pop(0)
    print(f"Player 1 plays: {player_1_card}")
    print(f"Player 2 plays: {player_2_card}")

    if len(player_1_deck) >= player_1_card and len(player_2_deck) >= player_2_card:
        # Here comes recursive combat
        print("Entering the subcombat...")
        sub_played_decks = []
        sub_player_1_deck = player_1_deck[:player_1_card]
        sub_player_2_deck = player_2_deck[:player_2_card]
        while sub_player_1_deck and sub_player_2_deck:
            winner = play_round(sub_played_decks, sub_player_1_deck, sub_player_2_deck)
            if winner == 11:
                break
        if winner == 1 or winner == 11:
            player_1_deck.extend([player_1_card, player_2_card])
        elif winner == 2:
            player_2_deck.extend([player_2_card, player_1_card])
    else:
        if player_1_card > player_2_card:
            print("Player 1 wins the round!")
            player_1_deck.extend([player_1_card, player_2_card])
            return 1
        else:
            print("Player 2 wins the round!")
            player_2_deck.extend([player_2_card, player_1_card])
            return 2


def find_winners_deck(winner):
    if winner == 1 or winner == 11:
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
    played_decks = []
    while player_1_deck and player_2_deck:
        print("\n")
        print(f"--- Round {counter} ---")
        winner = play_round(played_decks, player_1_deck, player_2_deck)
        if winner == 11:
            break
        counter += 1

    print("\n")
    print("== Post-game results ==")
    print(f"Player 1's deck: {player_1_deck}")
    print(f"Player 2's deck: {player_2_deck}")
    print(f"Score is {count_result(find_winners_deck(winner))}")

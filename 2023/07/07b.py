import fileinput
from collections import Counter

hand_scores = {
    "five": 7,
    "four": 6,
    "full_house": 5,
    "three": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high": 1,
}

def evaluate(hand):
    # 32T3K
    c = Counter(hand)
    jokers = c["1"]
    two_most_common = c.most_common(2)
    card, highest_count = two_most_common[0]
    
    if hand == "11111":
        return hand_scores["five"]
    if card != "1":
        highest_count += jokers
    else:
        # the highest is joker
        second_card, second_highest = two_most_common[1]
        highest_count += second_highest

    if highest_count == 5:
        return hand_scores["five"]
    second_card, second_highest = two_most_common[1]

    if highest_count == 4:
        return hand_scores["four"]
    elif highest_count == 3 and second_highest == 2:
        return hand_scores["full_house"]
    elif highest_count == 3 and second_highest == 1:
        return hand_scores["three"]
    elif highest_count == 2 and second_highest == 2:
        return hand_scores["two_pair"]
    elif highest_count == 2 and second_highest == 1:
        return hand_scores["one_pair"]
    else:
        return hand_scores["high"]


def replace_letters(hand):
    return hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "1").replace("T", "U")


if __name__ == "__main__":
    raw_data = {line.strip().split(" ")[0]: int(line.strip().split(" ")[1]) for line in fileinput.input()}
    scores = {}
    for hand, bid in raw_data.items():
        hand = replace_letters(hand)
        scores.setdefault(evaluate(hand), []).append({hand: bid})
    
    for hands in scores.values():
        hands.sort(key=lambda x: list(x.keys()))

    sorted_dict = {k: scores[k] for k in sorted(scores)}

    cnt = 0
    sorted_hands = []
    for rank, hands in sorted_dict.items():
        for hand_bid in hands:
            for hand, bid in hand_bid.items():
                sorted_hands.append(bid)

    for rank, bid in enumerate(sorted_hands, start=1):
        cnt += rank*bid

    print(cnt)


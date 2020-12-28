label = [int(char) for char in "219347865"]
label.extend([x for x in range(10, 1_000_001)])

# Create dict - element + its immediate neighbour
cups = {}
for i, element in enumerate(label):
    if element == label[-1]:
        cups[element] = label[0]
    else:
        cups[element] = label[i+1]


# Get current cup
# Get three to pick up
# Find destination cup
# Insert picked cups => change neighbours
# Neighbours to change:
# current cup -> old neighbour of 3rd picked cup
# destination cup -> 1st picked cup
# 3rd picked cup -> old neighbour of destination cup

min_val = min(label)
max_val = max(label)
current_cup = label[0]

for i in range(10_000_000):
    p1 = cups[current_cup]
    p2 = cups[p1]
    p3 = cups[p2]
    # print("current cup", current_cup)
    # print("picked up", p1, p2, p3)

    # Find destination cup
    dest_cup = current_cup - 1
    while True:
        if dest_cup in (p1, p2, p3):
            dest_cup -= 1
        elif dest_cup < min_val:
            dest_cup = max_val
        else:
            break

    # print("destination cup", dest_cup)

    to_change_1 = cups[p3]
    to_change_2 = p1
    to_change_3 = cups[dest_cup]

    cups[current_cup] = to_change_1
    cups[dest_cup] = to_change_2
    cups[p3] = to_change_3

    current_cup = cups[current_cup]


one = cups[1]
two = cups[one]
print(one * two)

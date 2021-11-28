def evaluate(turn, number):
    # Get tuple with last two turns the number was seen
    val = seen_numbers.get(number)
    # I've seen this number just once (its 1st value is 0)
    if val[0] == 0:
        # I've seen it once -> 0 is the next number
        # + update values for 0 in the seen_numbers
        old_val = seen_numbers[0]
        new_val = (old_val[1], turn)
        seen_numbers[0] = new_val
        return 0
    # I've seen this number more than once
    else:
        # Compute new number from the old values
        next_number = val[1] - val[0]
        # Update new number vals - it's being seen right now
        old_val = seen_numbers.get(next_number)
        # If number wasn't known before, add the 1st occurence
        if not old_val:
            new_val = (0, turn)
        else:
            new_val = (old_val[1], turn)
        seen_numbers[next_number] = new_val
        return next_number


starting = [0, 5, 4, 1, 10, 14, 7]
seen_numbers = {}

# Fill in the structure with starting values
# Value is tuple with two last turns the number was seen
# If number was seen just once, fill in 0 as 1st tuple value
for i, val in enumerate(starting, start=1):
    seen_numbers[val] = (0, i)

next_round = len(starting) + 1
number = evaluate(next_round, starting[-1])
while True:
    next_round += 1
    number = evaluate(next_round, number)
    if next_round == 30000000:
        print(number)
        break

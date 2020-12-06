"""
The list in 'test' represents answers from five groups:
    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?
"""
with open("input_6") as f:
    contents = f.read().split("\n\n")

yes_count = 0
for group in contents:
    # Create list of answers of each group separately
    splitted = group.strip().split("\n")
    ppl_in_group = len(splitted)
    # Sort all answers in one big list
    all_answers = sorted(''.join(splitted))
    matching_answers = []
    # Letters which are repeated in each answer are added to matching_answers
    for letter in all_answers:
        if all_answers.count(letter) == ppl_in_group:
            matching_answers.append(letter)
    # Use set to get rid of duplicates
    matching_answers = set(matching_answers)
    yes_count += len(matching_answers)

print(f"Everyone answered 'yes' to {yes_count} questions.")

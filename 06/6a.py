"""
The list in 'test' represents answers from five groups:
    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes".
"""

with open("input_6") as f:
    contents = f.read().split("\n\n")

# Remove newlines from the items in list
for group in contents:
    rejoined = "".join(group.split("\n"))
    contents[contents.index(group)] = rejoined

# Use set to count unique characters in each group
yes_count = 0
for answer in contents:
    yes_count += len(set(answer))

print(f"Sum of all positive questions is {yes_count}.")

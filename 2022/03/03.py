import fileinput

data = [line.strip() for line in fileinput.input()]

abc = "abcdefghijklmnopqrstuvwxyz"
abc += abc.upper()

total = 0
for rucksack in data:
    comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for letter in comp1:
        if letter in comp2:
            total += abc.index(letter) + 1
            break

print(total)
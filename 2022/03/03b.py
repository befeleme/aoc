import fileinput

data = [line.strip() for line in fileinput.input()]

abc = "abcdefghijklmnopqrstuvwxyz"
abc += abc.upper()


total = 0
for rucksack, i in zip(data[::3], range(0,len(data)+1,3)):
    for letter in rucksack:
        if (letter in data[i+1]) and (letter in data[i+2]):
            total += abc.index(letter)+1
            break

print(total)
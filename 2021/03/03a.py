import fileinput

report_numbers = [line.strip() for line in fileinput.input()]

gamma = ""
epsilon = ""
for i in range(len(report_numbers[0])):
    zeros = 0
    ones = 0
    for entry in report_numbers:
        if entry[i] == "0":
            zeros += 1
        else:
            ones += 1
    else:
        if zeros > ones:
            gamma += "0"
            epsilon += "1"
        else:
            epsilon += "0"
            gamma += "1"

print(int(gamma, 2) * int(epsilon, 2))

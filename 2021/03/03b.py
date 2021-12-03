import fileinput

report_numbers = [line.strip() for line in fileinput.input()]

oxygen_generator_rating = ""
co2_scrubber_rating = ""
lookout_copy_oxy = list(report_numbers)
lookout_copy_co2 = list(report_numbers)
for i in range(len(report_numbers[0])):
    zeros = 0
    ones = 0

    # oxygen
    for entry in lookout_copy_oxy:

        if entry[i] == "0":
            zeros += 1
        else:
            ones += 1
    else:
        if zeros > ones:
            lookout_copy_oxy = [x for x in lookout_copy_oxy if x[i] == "0"]

        else:
            lookout_copy_oxy = [x for x in lookout_copy_oxy if x[i] == "1"]

        if len(lookout_copy_oxy) == 1:
            oxygen_generator_rating = lookout_copy_oxy[0]

    # co2
    zeros = 0
    ones = 0
    for entry in lookout_copy_co2:

        if entry[i] == "0":
            zeros += 1
        else:
            ones += 1
    else:
        if zeros > ones:
            lookout_copy_co2 = [x for x in lookout_copy_co2 if x[i] == "1"]

        else:
            lookout_copy_co2 = [x for x in lookout_copy_co2 if x[i] == "0"]

        if len(lookout_copy_co2) == 1:
            co2_scrubber_rating = lookout_copy_co2[0]


print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))




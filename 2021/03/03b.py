import fileinput


def find_rating(rating, leading_value, index=0):
    bits = ("0", "1") if leading_value == "most_common_bits" else ("1", "0")

    if len(rating) == 1:
        return rating[0]

    zeros, ones = count_zeros_and_ones(rating, index)
    if zeros > ones:
        rating = [x for x in rating if x[index] == bits[0]]
    else:
        rating = [x for x in rating if x[index] == bits[1]]

    index += 1
    return find_rating(rating, leading_value, index)


def count_zeros_and_ones(rating, index):
    zeros = ones = 0
    for entry in rating:
        if entry[index] == "0":
            zeros += 1
        else:
            ones += 1
    return zeros, ones


report_numbers = [line.strip() for line in fileinput.input()]

oxygen_generator_rating = find_rating(list(report_numbers), "most_common_bits")
co2_scrubber_rating = find_rating(list(report_numbers), "least_common_bits")

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))

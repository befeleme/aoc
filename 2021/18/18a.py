import fileinput


def add(x, y):
    # [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]]
    # join with comma and add another pair of parentheses
    return "[" + x + "," + y + "]"

def exploding_index(sfnumber):
    depth = 0
    exploding_pair = ""
    for i, char in enumerate(sfnumber):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        # print(char, depth)

        if depth >= 5 and char in "0123456789":
            exploding_pair_left_number_index = i
            return exploding_pair_left_number_index
    return None

def explode(sfnumber, exploding_pair_left_number_index):
    new_sfnumber = ""
    # print(exploding_pair_left_number_index)

    if sfnumber[exploding_pair_left_number_index+1] in "0123456789":
        exploding_left = int(sfnumber[exploding_pair_left_number_index:exploding_pair_left_number_index+2])
        right_start = 3
    else:
        exploding_left = int(sfnumber[exploding_pair_left_number_index])
        right_start = 2
    print("exploding left", exploding_left)
    print(right_start)

    if sfnumber[exploding_pair_left_number_index+right_start+1] in "0123456789":
        exploding_right = int(sfnumber[exploding_pair_left_number_index+right_start:exploding_pair_left_number_index+right_start+2])
    else:
        exploding_right = int(sfnumber[exploding_pair_left_number_index+right_start])
    print("exploding right", exploding_right)

    # Go as far as possible, get the closest left number possible or None if none
    left_neighbour = None
    left_neighbour_index = None
    for i, char in enumerate(sfnumber[:exploding_pair_left_number_index]):
        if char in "0123456789":
            next_char = sfnumber[:exploding_pair_left_number_index][i+1]
            if next_char in "0123456789":
                left_neighbour = int(char + next_char)
            else:
                left_neighbour = int(char)
            left_neighbour_index = i
    print(left_neighbour, left_neighbour_index)
    # Break after the first found number - get the closest one, or None if none
    right_neighbour = None
    right_neighbour_index = None
    for i, char in enumerate(sfnumber[exploding_pair_left_number_index+right_start+1:]):
        if char in "0123456789":
            next_char = sfnumber[exploding_pair_left_number_index+right_start+1:][i+1]
            if next_char in "0123456789":
                right_neighbour = int(char + next_char)
            else:
                right_neighbour = int(char)
            right_neighbour_index = exploding_pair_left_number_index+right_start+1+i
            break
    print(right_neighbour, right_neighbour_index)



    # try to combine new snailfish number
    # count the numbers after exploding
    new_left = new_right = None
    if left_neighbour is not None:
        new_left = left_neighbour + exploding_left
    if right_neighbour is not None:
        new_right = right_neighbour + exploding_right

    print(new_left, new_right)
    # try to combine the reduced characters
    if new_left is None:
        # if len(str(new_right)) == 1:
        new_sfnumber = sfnumber[:exploding_pair_left_number_index-1] + "0" + sfnumber[exploding_pair_left_number_index+4:right_neighbour_index] + f"{new_right}" + sfnumber[right_neighbour_index+1:]
        # elif len(str(new_right)) == 2:
            # new_sfnumber = sfnumber[:exploding_pair_left_number_index-1] + f"0,{new_right}" + sfnumber[right_neighbour_index+1:]
    else:
        if new_right is None:
            # if len(str(new_left)) == 1:
            #     new_sfnumber = sfnumber[:left_neighbour_index] + f"{new_left}," + sfnumber[exploding_pair_left_number_index+4:]
            # elif len(str(new_left)) == 2:
            new_sfnumber = sfnumber[:left_neighbour_index] + f"{new_left}" + sfnumber[left_neighbour_index+1:exploding_pair_left_number_index-1] + "0" + sfnumber[exploding_pair_left_number_index+2+right_start:]
        else:
            new_sfnumber = sfnumber[:left_neighbour_index] + f"{new_left}" + sfnumber[left_neighbour_index+1:exploding_pair_left_number_index-1] + "0" + sfnumber[exploding_pair_left_number_index+2+right_start:right_neighbour_index] + f"{new_right}" + sfnumber[right_neighbour_index+1:]

            # new_sfnumber = sfnumber[:left_neighbour_index] + f"{new_left},0" + sfnumber[exploding_pair_left_number_index+4:right_neighbour_index] + f"{new_right}" + sfnumber[right_neighbour_index+1:]

    # print(new_sfnumber)
    return new_sfnumber

def split_index(sfnumber):
    depth = 0
    for i, char in enumerate(sfnumber):
        if char in "0123456789":
            if sfnumber[i+1] in "0123456789":
                return i
    return None


def split_complex(sfnumber, complex_no_index):
    tosplit = int(sfnumber[complex_no_index:complex_no_index+2])
    # print(tosplit)
    left_number = tosplit // 2
    right_number = tosplit - left_number

    new_sfnumber = sfnumber[:complex_no_index] + f"[{left_number},{right_number}]" + sfnumber[complex_no_index+2:]

    # print(new_sfnumber)
    return new_sfnumber


def reduce(a, b):
    # First, add:
    partial = add(a, b)
    print("added", partial)
    # Then, check if explosion is possible
    # exploding_ind = exploding_index(partial)
    # print(exploding_ind)
    while True:
        while (exploding_ind := exploding_index(partial)):
            print("explode?", exploding_ind)
            # exploding_index = exploding_index(partial)
            # if exploding_ind is not None:
            partial = explode(partial, exploding_ind)
            print(partial)
            exploding_ind = exploding_index(partial)
            print("explode 2?", exploding_ind)

        # print(exploding_ind)
        # Then, check if split is possible
        if (split_ind := split_index(partial)):
            print("split?", split_ind)
            partial = split_complex(partial, split_ind)
            print(partial)
        # print(exploding_ind, split_ind)
        if exploding_ind is None and split_ind is None:
            print(partial)
            break
    return partial

# print(reduce("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")


data = [line.strip() for line in fileinput.input()]
# print(data)

res = reduce(data[0], data[1])
# print(res)

for i, number in enumerate(data[2:]):
    res = reduce(res, number)
    print(res)

# i = "[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[0,[11,3]],[[6,3],[8,8]]]]]"
# e = exploding_index(i)
# res = explode(i, e)

# print(exploding_index(res))
print(res == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")

# print(exploding_index("[[[[[9,8],1],2],3],4]"), True)
# print(exploding_index("[[[[9,8],1],2],3],4"), False)
# print(exploding_index("[[[[9,8],[5,1],2],3],[[[3,4]]]"), False)
# print(exploding_index("[[[[9,8],[5,1],2],3],[[[[3,4]]]]"), True)

# testno = "[[[[[9,8],1],2],3],4]"
# expl = exploding_index(testno)

# print(explode("[[[[[9,8],1],2],3],4]", expl) == "[[[[0,9],2],3],4]")

# expl = exploding_index("[7,[6,[5,[4,[3,2]]]]]")
# res = explode("[7,[6,[5,[4,[3,2]]]]]", expl)
# print("res", res)
# print(res == "[7,[6,[5,[7,0]]]]")

# expl = exploding_index("[[6,[5,[4,[3,2]]]],1]")
# print(explode("[[6,[5,[4,[3,2]]]],1]", expl) == "[[6,[5,[7,0]]],3]")

# n = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# expl = exploding_index(n)
# print(explode(n, expl) == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")

# n = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
# expl = exploding_index(n)
# res = explode(n, expl)
# print(res)
# print(res == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

# spl = split_index("[[[[0,7],4],[15,[0,13]]],[1,1]]")
# r = split_complex("[[[[0,7],4],[15,[0,13]]],[1,1]]", spl)
# print(r == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
# spl = split_index(r)
# s = split_complex(r, spl)
# print(s == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")



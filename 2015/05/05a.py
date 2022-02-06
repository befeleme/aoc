from pathlib import Path

def is_nice_part_1(string):
    if has_three_vowels(string) and has_repeated_next_letter(string) and has_allowed_string(string):
        return True
    return False

def is_nice_part_2(string):
    if has_pair_twice(string) and has_repeated_second_next(string):
        return True
    return False

def has_three_vowels(string):
    vowels = "aeiou"
    if sum([string.count(vowel) for vowel in vowels]) >= 3:
        return True
    return False

def _has_repeated_letter(string, pos):
    for i, letter in enumerate(string):
        try:
            if string[i+pos] == letter:
                return True
        except IndexError:
            return False

def has_repeated_next_letter(string):
    return _has_repeated_letter(string, 1)

def has_repeated_second_next(string):
    # xyx, abcdefeghi (efe), or even aaa
    return _has_repeated_letter(string, 2)

def has_allowed_string(string):
    for combo in "ab", "cd", "pq", "xy":
        if combo in string:
            return False
    return True

def has_pair_twice(string):
    # xyxy (xy) or aabcdefgaa (aa), but not aaa (aa, but it overlaps)
    start = 0
    while True:
        pair = string[start:start+2]
        if len(pair) <= 1:
            return False
        sub_start = start+2
        while True:
            to_check = string[sub_start:sub_start+2]
            # reached the end of the string
            if len(to_check) <= 1:
                break
            if pair == to_check:
                return True
            sub_start += 1
        start += 1


if __name__ == "__main__":
    strings = Path('input').read_text().split()

    # The typical round of indented for/if clause with counter
    # can be contracted to list comprehension
    print(sum([1 for string in strings if is_nice_part_1(string)]))
    print(sum([1 for string in strings if is_nice_part_2(string)]))

    # ...or even more readable: with map() usage
    print(sum(map(is_nice_part_1, strings)))
    print(sum(map(is_nice_part_2, strings)))


    # AoC test examples
    assert is_nice_part_1("ugknbfddgicrmopn") == True
    assert is_nice_part_1("aaa") == True
    assert is_nice_part_1("jchzalrnumimnmhp") == False
    assert is_nice_part_1("haegwjzuvuyypxyu") == False
    assert is_nice_part_1("dvszwmarrgswjxmb") == False
    assert has_pair_twice("xyxy") == True
    assert has_pair_twice("aabcdefgaa") == True
    assert has_pair_twice("aaa") == False
    assert is_nice_part_2("qjhvhtzxzqqjkmpb") == True
    assert is_nice_part_2("xxyxx") == True
    assert is_nice_part_2("ieodomkazucvgmuy") == False
    assert is_nice_part_2("uurcxstgmygtbstg") == False
    
# functions use type annotations
# to run: 
# $ pip install mypy
# $ mypy 11a.py

VALID_LEN = 8
VALID_CHARS = 'abcdefghijklmnopqrstvwuxyz'


def increment(password: str, partial_password: str ='') -> str:
    last_char = password[-1]
    try:
        new_last_char = VALID_CHARS[VALID_CHARS.index(last_char) + 1]
        new_password = password[:-1] + new_last_char
    except IndexError:  # the last_char was 'z'
        new_last_char = 'a'
        partial_password += increment(password[:-1], partial_password=partial_password)
        new_password = partial_password + new_last_char
    return new_password


def chars_are_consecutive(password: str) -> bool:
    """Passwords must include one increasing straight of at least three letters,
    like abc, bcd, cde, and so on, up to xyz.
    They cannot skip letters; abd doesn't count.
    """

    for i, char in enumerate(password[:-2]):
        if char + password[i+1] + password[i+2] in VALID_CHARS:
            return True
    return False


def i_o_l_are_not_in_password(password: str) -> bool:
    """Passwords may not contain the letters i, o, or l, 
    as these letters can be mistaken for other characters and are therefore confusing.
    """

    for char in 'i', 'l', 'o':
        if char in password:
            return False
    return True


def double_chars_are_present(password: str) -> bool:
    """Passwords must contain at least two different,
    non-overlapping pairs of letters, like aa, bb, or zz.
    """

    counter = 0
    for i, char in enumerate(password[:-1]):
        if char == password[i+1]:
            if i == 0:
                counter += 1
            elif char != password[i-1]:
                counter += 1
    if counter >= 2:
        return True
    return False
    

def validate(password: str) -> bool:
    if chars_are_consecutive(password) and \
        i_o_l_are_not_in_password(password) and \
        double_chars_are_present(password) and \
        len(password) == VALID_LEN:
        return True
    return False


def main() -> None:
    password = 'vzbxxyzz'
    new_password = increment(password)
    while not validate(new_password):
        new_password = increment(new_password)
    print(new_password)

# Tests
assert increment('abzz') == 'acaa'
assert increment('abx') == 'aby'
assert chars_are_consecutive('hijklmmn') is True
assert chars_are_consecutive('hxjkxmmn') is False
assert i_o_l_are_not_in_password('abbceffg') is True
assert i_o_l_are_not_in_password('ghijklmn') is False
assert double_chars_are_present('abcdffaa') is True
assert double_chars_are_present('ghijklmn') is False
assert double_chars_are_present('hiklmggg') is False


if __name__ == '__main__':
    main()

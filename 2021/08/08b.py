import fileinput
import re

data = [line.strip() for line in fileinput.input()]


def process(signals, output):
    one = signals[0]
    seven = signals[1]
    four = signals[2]
    eight = signals[-1]

    a = (seven - one)
    for signal in signals[3:-1]:
        if (four | seven <= signal) and len(signal) == 6:
            g = signal - (four | seven)
    e = eight - (four | seven | g)
    for signal in signals[3:-1]:
        if ((one | a | g) <= signal) and len(signal) == 5:
            d = signal - (one | a | g)
    for signal in signals[3:-1]:
        if ((seven | e | g) <= signal) and len(signal) == 6:
            b = signal - (seven | e | g)
    for signal in signals[3:-1]:
        if ((a | b | d | e | g) <= signal) and len(signal) == 6:
            f = signal - (a | b | d | e | g)
    c = eight - (a | b | d | e | f | g)

    digits = {
        "0": eight - d,
        "1": one,
        "2": a | c | d | e | g,
        "3": a | c | d | f | g,
        "4": four,
        "5": a | b | d | f | g,
        "6": eight - c,
        "7": seven,
        "8": eight,
        "9": eight - e,
    }

    o = ""
    for digit in output:
        for k, v in digits.items():
            if digit == v:
                o += k
    return int(o)


counter = 0
pattern = r"(\w{2,7})"
for line in data:
    res = re.findall(pattern, line)
    signals = res[:10]
    output = res[-4:]
    signals = sorted(signals, key=lambda x: len(x))
    signals = [set(x) for x in signals]
    output = [set(x) for x in output]
    decoded = process(signals, output)
    counter += decoded


print(counter)

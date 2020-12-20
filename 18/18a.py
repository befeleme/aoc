import re
import fileinput


def eval_parenthesis(inp):
    if "(" not in inp and ")" not in inp:
        return inp
    start = inp.find("(")
    next_start = inp.find("(", start+1)
    end = inp.find(")")
    if next_start == -1:
        pass
    elif next_start < end:
        start = next_start
    res = eval_straight(inp[start+1:end])
    out = inp[:start] + str(res) + inp[end+1:]
    return eval_parenthesis(out)


def eval_straight(inp):
    matched = re.findall(r'([\*\+]) (\d+)', inp)
    start = re.match(r'^\d+', inp).group()
    for match in matched:
        res = eval(start+match[0]+match[1])
        start = str(res)
    return res


def evaluate_expression(exp):
    return eval_straight(eval_parenthesis(exp))


examples = [x.strip() for x in fileinput.input()]

total = 0
for example in examples:
    res = evaluate_expression(example)
    total += int(res)

print("total", total)

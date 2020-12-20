import re
import fileinput


def eval_parenthesis(inp):
    if "(" not in inp and ")" not in inp:
        return inp
    start = inp.find("(")
    next_start = inp.find("(", start+1)
    end = inp.find(")")
    # Find returns -1 when no match!
    if next_start == -1:
        pass
    elif next_start < end:
        start = next_start
    res = eval_straight(inp[start+1:end])
    out = inp[:start] + str(res) + inp[end+1:]
    return eval_parenthesis(out)


def eval_straight(inp):
    matched_add = re.search(r'(\d+ \+ \d+)', inp)
    if matched_add:
        new_inp = eval_tiniest(inp, matched_add)
        return eval_straight(new_inp)
    else:
        matched_mul = re.search(r'\d+ \* \d+', inp)
        if not matched_mul:
            return inp
        new_inp = eval_tiniest(inp, matched_mul)
        return eval_straight(new_inp)


def eval_tiniest(inp, matched):
    res = eval(matched.group())
    out = inp[:matched.span()[0]] + str(res) + inp[matched.span()[1]:]
    return out


def evaluate_expression(exp):
    return eval_straight(eval_parenthesis(exp))


examples = [x.strip() for x in fileinput.input()]

total = 0
for example in examples:
    res = evaluate_expression(example)
    total += int(res)

print("total", total)

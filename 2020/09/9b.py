import fileinput


contents = [int(line.strip()) for line in fileinput.input()]


def find_contiguous_set(start, end):
    while True:
        if end == len(contents):
            return
        elif sum(contents[start:end]) == 675280050:
            return min(contents[start:end]) + max(contents[start:end])
        else:
            start += 1
            end += 1


end_span = 3
while True:
    result = find_contiguous_set(0, end_span)
    if not result:
        end_span += 1
    else:
        print(result)
        break

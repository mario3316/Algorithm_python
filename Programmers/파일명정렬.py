def parse_string(s: str):
    i = 0
    head = 0
    # HEAD
    while i < len(s):
        if s[i].isnumeric():
            head = i
            break
        i += 1

    # NUMBER
    while i < len(s):
        if not s[i].isnumeric():
            break
        i += 1

    return s[0:head].lower(), int(s[head:i])


def solution(files):
    answer = []
    for i in range(0, len(files)):
        head, number = parse_string(files[i])
        answer.append([files[i], head, number, i])

    answer = sorted(answer, key=lambda x: (x[1], x[2], x[3]))
    return [file[0] for file in answer]

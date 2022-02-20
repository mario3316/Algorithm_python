def parse(s):
    result = []
    s = s[2:-2].split("},{")
    for i in s:
        temp = []
        t = i.split(",")
        for j in t:
            temp.append(int(j))
        result.append(temp)
    return result


def solution(s):
    s = parse(s)
    a = [0 for _ in range(len(s))]
    s.sort(key=len)

    for i, v in enumerate(s):
        if i > 0:
            a[i] = list(set(v) - set(s[i - 1]))[0]
        else:
            a[i] = v[0]

    return a


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")

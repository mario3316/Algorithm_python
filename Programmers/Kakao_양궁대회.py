from itertools import combinations_with_replacement


def get_list_of_lower(a, b):
    for i in reversed(range(11)):
        if a[i] > b[i]:
            return a
        elif a[i] == b[i]:
            continue
        else:
            return b


def calc_points(ryan, apeach):
    ryan_point = 0
    apeach_point = 0

    for i in range(11):
        if ryan[i] > apeach[i]:
            ryan_point += 10 - i
        else:
            if not ryan[i] == 0 or not apeach[i] == 0:
                apeach_point += 10 - i

    return ryan_point - apeach_point


def solution(n, info):
    answer = [-1]
    max_point = 0

    for i in combinations_with_replacement(range(11), n):
        print(i)
        selected = [0 for _ in range(11)]
        for j in i:
            selected[j] += 1
        point = calc_points(selected, info)
        if point > max_point:
            max_point = point
            answer = selected
        elif point == max_point and point != 0:
            answer = selected if answer[0] == -1 else get_list_of_lower(answer, selected)

    return answer

# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))

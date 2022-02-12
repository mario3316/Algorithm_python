# 통계학
# 정렬
import sys
from collections import Counter


def get_average(target: list) -> int:
    return round(sum(target) / len(target))


def get_middle(target: list) -> int:
    return target[len(target) // 2]


def get_mode(target: list) -> int:
    count = Counter(target).most_common(2)
    if len(target) == 1:
        return target[0]
    return count[0][0] if count[0][1] != count[1][1] else count[1][0]


# def get_mode(target: list) -> int:
#     if len(target) == 1:
#         return target[0]
#
#     count = {}
#     for i in target:
#         if count.get(i) is None:
#             count[i] = 1
#         else:
#             count[i] = count[i] + 1
#
#     # 우선순위 : value(내림차순) -> key(오름차순)
#     sorted_dict = sorted(count.items(), key=lambda x: (-x[1], x[0]))
#     return sorted_dict[0][0] if sorted_dict[0][1] != sorted_dict[1][1] else sorted_dict[1][0]


def get_range(target: list) -> int:
    return abs(max(target) - min(target))


def solve(target: list):
    target.sort()
    print(get_average(target))
    print(get_middle(target))
    print(get_mode(target))
    print(get_range(target))


if __name__ == "__main__":
    num_list = []
    N = int(input())
    for _ in range(N):
        num_list.append(int(sys.stdin.readline()))
    solve(num_list)

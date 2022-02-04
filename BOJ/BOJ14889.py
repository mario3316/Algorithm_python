# 스타트와 링크
# 완전탐색, Brute Force
from itertools import combinations, permutations


def calc_score(arr: list, team: tuple) -> int:
    sum = 0
    comb = list(permutations(team, 2))

    for i in comb:
        sum += arr[i[0] - 1][i[1] - 1]

    return sum


def solve(N: int, arr: list) -> None:
    item = [x for x in range(1, N + 1)]
    min = float('inf')

    team1 = list(combinations(item, N // 2))
    team2 = [tuple(set(item) - set(t)) for t in team1]

    for i in range(len(team1)):
        score = abs(calc_score(arr, team1[i]) - calc_score(arr, team2[i]))
        min = score if score < min else min

    print(min)


if __name__ == "__main__":
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]
    solve(N, arr)

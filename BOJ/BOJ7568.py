# 덩치
# Brute Force
def is_bigger(origin: list, target: list) -> bool:
    if origin[0] < target[0] and origin[1] < target[1]:
        return True
    else:
        return False


def solve(n: int, m: list) -> None:
    for i in range(len(m)):
        rank = 1
        for j in range(len(m)):
            if i is not j and is_bigger(m[i], m[j]):
                rank += 1
        print(rank, end=" ")


if __name__ == "__main__":
    N = int(input())
    M = [[int(x) for x in input().split()] for _ in range(N)]
    solve(N, M)

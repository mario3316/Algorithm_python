# 좌표 정렬하기
# 정렬
import sys


def solve(target: list) -> None:
    target = sorted(target, key=lambda x: (x[0], x[1]))
    for x, y in target:
        print(x, y)


if __name__ == "__main__":
    axis = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        x, y = sys.stdin.readline().split()
        axis.append((int(x), int(y)))

    solve(axis)

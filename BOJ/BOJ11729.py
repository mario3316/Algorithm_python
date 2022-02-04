# 하노이 탑 이동 순서
# 재귀

def hanoi(n: int, start: int, target: int) -> int:
    other = 6 - start - target

    if n >= 1:
        hanoi(n - 1, start, other)
        print(start, target)
        hanoi(n - 1, other, target)
    else:
        return


if __name__ == "__main__":
    N = int(input())
    print(pow(2, N) - 1)
    result = hanoi(N, 1, 3)

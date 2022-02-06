# 영화감독 숌
# Brute Force
def solve(n: int) -> None:
    i = 666
    count = 0
    while True:
        if '666' in str(i):
            count += 1
        if count == n:
            print(i)
            break
        i += 1


if __name__ == "__main__":
    N = int(input())
    solve(N)

# Yonsei TOTO
# 그리디
def solve() -> int:
    required_mileage = []
    result = 0

    n, m = [int(x) for x in input().split()]

    for i in range(n):
        P, L = [int(x) for x in input().split()]
        current = [int(x) for x in input().split()]

        if P < L:
            required_mileage.append(1)
            continue
        else:
            current.sort(reverse=True)
            required_mileage.append(current[L - 1])

    required_mileage.sort()
    for i in required_mileage:
        if m - i >= 0:
            m -= i
            result += 1
        else:
            break

    return result


if __name__ == "__main__":
    print(solve())

import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2
    count = 0
    for l in lines:
        count += l // mid

    if count < N:
        right = mid - 1
    else:
        left = mid + 1

print(right)

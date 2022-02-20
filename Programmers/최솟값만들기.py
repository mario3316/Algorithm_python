def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = sum([a * b for a, b in zip(A, B)])
    return answer


print(solution([1, 4, 2], [5, 4, 4]))

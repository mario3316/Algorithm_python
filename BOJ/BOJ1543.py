# 문서검색
# 그리디 (앞부터 먼저 차근차근 찾아나가야 최대로 중복시킬수 있음)

def solve(target: str, keyword: str) -> int:
    answer = 0
    i = 0

    while len(target) > 0:
        idx = target.find(keyword)
        if idx == -1:
            break
        else:
            answer += 1
            target = target[idx + len(keyword):]

    return answer


if __name__ == "__main__":
    ans = solve(input(), input())
    print(ans)

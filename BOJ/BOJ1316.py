# 그룹단어 체커
# 문자열
def is_group_word(target: str) -> bool:
    found = set()
    for i in range(len(target)):
        if i == 0:
            found.add(target[i])
        else:
            if target[i] != target[i - 1] and target[i] in found:
                return False
            else:
                found.add(target[i])

    return True


def solve() -> int:
    result = 0
    N = int(input())

    for i in range(N):
        s = input()
        if is_group_word(s):
            result += 1

    return result


if __name__ == "__main__":
    print(solve())

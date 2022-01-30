# 수 찾기
# set(hashset)을 쓰지 않으면 시간초과

def solve(nl: set, ml: list) -> None:
    for x in ml:
        if x in nl:
            print('1')
        else:
            print('0')


if __name__ == "__main__":
    N = int(input())
    n_list = [int(x) for x in input().split()]
    M = int(input())
    m_list = [int(x) for x in input().split()]

    solve(set(n_list), m_list)

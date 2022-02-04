# 크로아티아 알파벳
# 문자열
def solve(s: str) -> None:
    replace_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for i in replace_list:
        s = s.replace(i, '0')

    print(len(s))


if __name__ == "__main__":
    solve(input())

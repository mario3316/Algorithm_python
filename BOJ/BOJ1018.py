# 체스판 다시 칠하기
# Brute Force
import copy


def count_wrong_blocks(r: int, c: int, start: int, board: list) -> int:
    result = 0

    if board[r][c] != start:
        result += 1
        board[r][c] = start

    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if j == c and i != r:
                if board[i][j] == board[i - 1][j]:
                    result += 1
                    board[i][j] = 0 if board[i - 1][j] == 1 else 1

            if j != c and board[i][j] == board[i][j - 1]:
                result += 1
                board[i][j] = 0 if board[i][j - 1] == 1 else 1

    return result


def solve(m: int, n: int, board: list) -> int:
    result = float('inf')

    for i in range(0, m - 7):
        for j in range(0, n - 7):
            result = min(result, count_wrong_blocks(i, j, 0, copy.deepcopy(board)))
            result = min(result, count_wrong_blocks(i, j, 1, copy.deepcopy(board)))

    return result


if __name__ == "__main__":
    M, N = [int(x) for x in input().split()]
    B = [[0 if x == 'W' else 1 for x in list(input())] for _ in range(M)]
    print(solve(M, N, B))

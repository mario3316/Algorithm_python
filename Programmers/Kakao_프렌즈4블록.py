def is_in(i, j, m, n):
    return 0 <= i < m and 0 <= j < n


def is_markable(i, j, m, n, board):
    cur = board[i][j]
    if cur is None:
        return False
    if not is_in(i, j + 1, m, n) or not is_in(i + 1, j, m, n) or not is_in(i + 1, j + 1, m, n):
        return False
    if board[i][j + 1] != cur:
        return False
    if board[i + 1][j] != cur:
        return False
    if board[i + 1][j + 1] != cur:
        return False
    return True


def mark_erasable_block(m, n, board):
    flag = False
    boolean = [[False for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if is_markable(i, j, m, n, board):
                boolean[i][j] = True
                boolean[i][j + 1] = True
                boolean[i + 1][j] = True
                boolean[i + 1][j + 1] = True
                flag = True

    return flag, boolean


def erase(m, n, boolean, board):
    count = 0
    for i in range(m):
        for j in range(n):
            if boolean[i][j]:
                board[i][j] = None
                count += 1
    return count


def drop_down(m, n, board):
    for j in range(n):
        for i in reversed(range(m - 1)):
            n_i = i
            for n in range(i + 1, m):
                if board[n][j] is None:
                    n_i = n
                else:
                    break
            if n_i != i:
                board[n_i][j] = board[i][j]
                board[i][j] = None


def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:
        flag, boolean = mark_erasable_block(m, n, board)
        if not flag:
            break
        else:
            answer += erase(m, n, boolean, board)
            drop_down(m, n, board)

    return answer

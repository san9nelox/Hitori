from hotori_logic.field import board, print_board


def solve_hitori(solved_board):
    board = [row[:] for row in solved_board]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 'x':
                # Проверяем, можно ли закрасить клетку
                if can_paint(board, i, j):
                    board[i][j] = 'x'
                else:
                    # Если нельзя, то ищем другую клетку
                    for k in range(i, -1, -1):
                        for l in range(n - 1, -1, -1):
                            if board[k][l] == 'x':
                                board[k][l] = 0
                                if can_paint(board, k, l):
                                    board[k][l] = 'x'
                                    break
                                else:
                                    board[k][l] = 'x'
                    if board[i][j] != 'x':
                        continue
    return board


def can_paint(board, i, j):
    n = len(board)
    # Проверяем, что клетка не соприкасается по стороне с другой закрашенной клеткой
    if i > 0 and board[i - 1][j] == 'x':
        return False
    if i < n - 1 and board[i + 1][j] == 'x':
        return False
    if j > 0 and board[i][j - 1] == 'x':
        return False
    if j < n - 1 and board[i][j + 1] == 'x':
        return False
    return True


result = solve_hitori(board)
print('\n\n\n')
print_board(result, len(result), len(result[0]))

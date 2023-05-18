from hitori_logic.field import board, print_board


def find_duplicates(arr_board, arr_col):
    # Проверяем строки
    for i in range(len(arr_board)):
        for j in range(len(arr_board[i])):
            if 0 < j < len(arr_board[i]) - 1 and arr_board[i][j - 1] == arr_board[i][j + 1]:
                arr_col[i][j] = 1
                arr_col[i][j - 1] = -1
                arr_col[i][j + 1] = -1

    # Проверяем столбцы
    for j in range(len(arr_board[0])):
        for i in range(len(arr_board)):
            if 0 < i < len(arr_board) - 1 and arr_board[i - 1][j] == arr_board[i + 1][j]:
                arr_col[i][j] = 1
                arr_col[i + 1][j] = -1
                arr_col[i - 1][j] = -1


array_colors = [[0] * len(board[0]) for i in range(len(board))]

find_duplicates(board, array_colors)
print('\n')
print_board(array_colors, len(array_colors), len(array_colors[0]))

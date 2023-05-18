from hitori_logic.field import print_board


def find_duplicates(arr_board, arr_col):
    # Проверяем строки
    for i in range(len(arr_board)):
        for j in range(len(arr_board[i])):
            if 0 < j < len(arr_board[i]) - 1 and arr_board[i][j - 1] == arr_board[i][j + 1]:
                arr_col[i][j] = 'w'
                arr_col[i][j - 1] = 'b'
                arr_col[i][j + 1] = 'b'

    # Проверяем столбцы
    for j in range(len(arr_board[0])):
        for i in range(len(arr_board)):
            if 0 < i < len(arr_board) - 1 and arr_board[i - 1][j] == arr_board[i + 1][j]:
                arr_col[i][j] = 'w'
                arr_col[i + 1][j] = 'b'
                arr_col[i - 1][j] = 'b'


board = [
    [2, 6, 3, 4, 5, 1, 6, 4, 4, 1],
    [2, 4, 5, 5, 6, 1, 3, 1, 4, 3],
    [1, 6, 1, 3, 4, 4, 4, 6, 2, 5],
    [3, 6, 6, 3, 1, 4, 3, 6, 4, 3],
    [3, 1, 5, 3, 2, 6, 6, 4, 6, 1],
    [6, 1, 1, 2, 4, 4, 6, 4, 6, 5]
]

print_board(board, len(board), len(board[0]))
array_colors = [['g'] * len(board[0]) for i in range(len(board))]
find_duplicates(board, array_colors)
print('\n')
print_board(array_colors, len(array_colors), len(array_colors[0]))
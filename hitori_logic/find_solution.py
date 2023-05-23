# from hitori_logic.field import board


def find_duplicates(arr_board, arr_col):
    # Проверяем строки
    for i in range(len(arr_board)):
        for j in range(len(arr_board[i])):
            if 0 < j < len(arr_board[i]) - 1 and arr_board[i][j - 1] == arr_board[i][j + 1] == arr_board[i][j]:
                arr_col[i][j] = 'w'
                arr_col[i][j - 1] = 'b'
                arr_col[i][j + 1] = 'b'

    # Проверяем столбцы
    for j in range(len(arr_board[0])):
        for i in range(len(arr_board)):
            if 0 < i < len(arr_board) - 1 and arr_board[i - 1][j] == arr_board[i + 1][j] == arr_board[i][j]:
                arr_col[i][j] = 'w'
                arr_col[i + 1][j] = 'b'
                arr_col[i - 1][j] = 'b'


def paint_neighbors_white(board_colors):
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'b':
                if i > 0:
                    is_black(board_colors[i - 1][j])
                    board_colors[i - 1][j] = 'w'
                if i < len(board_colors[i]) - 1:
                    is_black(board_colors[i + 1][j])
                    board_colors[i + 1][j] = 'w'
                if j > 0:
                    is_black(board_colors[i][j - 1])
                    board_colors[i][j - 1] = 'w'
                if j < len(board_colors) - 1:
                    is_black(board_colors[i][j + 1])
                    board_colors[i][j + 1] = 'w'


def paint_in_lines_black(board_colors, board):
    # Проверяем строки
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'w':
                for k in range(len(board_colors[i])):
                    if board[i][j] == board[i][k] and board_colors[i][k] != 'b' and j != k:
                        is_while(board_colors[i][k])
                        board_colors[i][k] = 'b'

    # Проверяем столбцы
    for j in range(len(board_colors[0])):
        for i in range(len(board_colors)):
            if board_colors[i][j] == 'w':
                for k in range(len(board_colors)):
                    if board[i][j] == board[k][j] and board_colors[k][j] != 'b' and k != i:
                        is_while(board_colors[k][j])
                        board_colors[k][j] = 'b'


def paint_single(board_colors, board):
    for i in range(len(board_colors)):
        for j in range(len(board_colors[i])):
            if board_colors[i][j] == 'g':
                can_paint = True
                for k in range(len(board_colors[0])):
                    if board[i][j] == board[i][k] and (board_colors[i][k] == 'g' or board_colors[i][k] == 'w') \
                            and k != j:
                        can_paint = False
                        break
                for k in range(len(board_colors)):
                    if board[i][j] == board[k][j] and (board_colors[k][j] == 'g' or board_colors[k][j] == 'w') \
                            and k != i:
                        can_paint = False
                        break
                if can_paint:
                    board_colors[i][j] = 'w'


def is_while(color):
    if color == 'w':
        exit('Головоломку невозможно решить')


def is_black(color):
    if color == 'b':
        exit('Головоломку невозможно решить')


def hitori_solution():
    board = [
        [1, 1, 6, 2, 5, 4, 2],
        [5, 6, 1, 2, 2, 2, 4],
        [3, 2, 5, 7, 7, 2, 1],
        [3, 5, 3, 3, 4, 7, 5],
        [1, 3, 4, 7, 7, 7, 6],
        [4, 4, 4, 5, 3, 1, 7],
        [6, 7, 2, 1, 2, 3, 7]
    ]
    for row in board:
        print(row)
    board_colors = [['g'] * len(board[0]) for i in range(len(board))]
    find_duplicates(board, board_colors)
    paint_neighbors_white(board_colors)
    print('\n')

    while True:
        is_painted = False
        for i in range(len(board_colors)):
            for j in range(len(board_colors[i])):
                if board_colors[i][j] == 'g':
                    is_painted = True
                    paint_in_lines_black(board_colors, board)
                    paint_neighbors_white(board_colors)
                    paint_single(board_colors, board)
        if not is_painted:
            break

    for row in board_colors:
        print(row)


hitori_solution()

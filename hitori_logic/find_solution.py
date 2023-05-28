from hitori_logic.field import generate, change_flag
import copy


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
                if i < len(board_colors) - 1:
                    is_black(board_colors[i + 1][j])
                    board_colors[i + 1][j] = 'w'
                if j > 0:
                    is_black(board_colors[i][j - 1])
                    board_colors[i][j - 1] = 'w'
                if j < len(board_colors[i]) - 1:
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


def paint_сontinuous_path(board_colors, i, j):
    board_colors[i][j] = 'b'
    if not check_connected_white(board_colors):
        board_colors[i][j] = 'g'


def check_connected_white(array):
    rows, cols = len(array), len(array[0])
    visited = set()  # Множество посещенных позиций
    stack = []  # Стек для обхода соседних элементов

    # Находим первую позицию 'w' или 'g'
    start_i, start_j = None, None
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == 'w':
                start_i, start_j = i, j
                break
        if start_i is not None:
            break

    if start_i is None or start_j is None:
        # Не удалось найти 'w' или 'g'
        return False

    stack.append((start_i, start_j))

    # Обходим соседние элементы
    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        # Проверяем соседей по горизонтали и вертикали
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and (array[nx][ny] == 'w' or array[nx][ny] == 'g') and (
                    nx, ny) not in visited:
                stack.append((nx, ny))

    # Проверяем, что все 'w' были посещены
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == 'w' and (i, j) not in visited:
                return False

    return True


def is_while(color):
    if color == 'w':
        raise AttributeError
        # exit('Головоломку невозможно решить - попытка закрасить черным белую клетку')


def is_black(color):
    if color == 'b':
        raise AttributeError
        # exit('Головоломку невозможно решить - попытка закрасить белым черную клетку')


def hitori_solution():
    board = generate()
    try:
        board_colors = [['g'] * len(board[0]) for _ in range(len(board))]
        find_duplicates(board, board_colors)
        paint_neighbors_white(board_colors)

        while True:
            is_painted = False
            for i in range(len(board_colors)):
                for j in range(len(board_colors[i])):
                    if board_colors[i][j] == 'g':
                        is_painted = True
                        prev_board_colors = copy.deepcopy(board_colors)
                        paint_in_lines_black(board_colors, board)
                        paint_neighbors_white(board_colors)
                        paint_single(board_colors, board)

                        if prev_board_colors == board_colors:
                            paint_сontinuous_path(board_colors, i, j)
            if not is_painted:
                break
            if prev_board_colors == board_colors:
                raise AttributeError
                # exit('Головоломку невозможно решить - маршрут нельзя построить')

        for row in board:
            print(row)
        print()
        for row in board_colors:
            print(row)
        change_flag()
    except AttributeError:
        hitori_solution()


"""
[1, 1, 6, 2, 5, 4, 2],
[5, 6, 1, 2, 2, 2, 4],
[3, 2, 5, 7, 7, 2, 1],
[3, 5, 3, 3, 4, 7, 5],
[1, 3, 4, 7, 7, 7, 6],
[4, 4, 4, 5, 3, 1, 7],
[6, 7, 2, 1, 2, 3, 7]
"""

"""
[5, 1, 3, 3, 2, 6],
[3, 4, 5, 1, 5, 3],
[6, 2, 4, 5, 3, 2],
[1, 3, 5, 6, 3, 2],
[3, 5, 1, 2, 6, 3],
[4, 1, 2, 3, 1, 5]
"""

"""
[6, 6, 2, 1, 5, 8, 3, 1],
[3, 5, 7, 4, 2, 8, 2, 6],
[6, 8, 7, 4, 8, 8, 2, 3],
[4, 8, 3, 1, 7, 5, 1, 2],
[8, 1, 5, 4, 4, 8, 6, 8],
[7, 3, 2, 5, 6, 2, 6, 4],
[6, 2, 4, 6, 1, 3, 7, 5],
[5, 7, 1, 1, 6, 5, 4, 5]
"""

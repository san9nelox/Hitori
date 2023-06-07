from hitori_logic.field import generate, change_flag, input_board
from settings.diagonal_neighbors import are_horiz_neigh_diff
import copy

final_board = None
final_board_color = None
is_generate = True


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


def paint_neighbors_horizontal_while(i, j, board_colors):
    if i > 0:
        if j > 0:
            is_black(board_colors[i - 1][j - 1])
            board_colors[i - 1][j - 1] = 'w'
        if j < len(board_colors[i]):
            is_black(board_colors[i - 1][j + 1])
            board_colors[i - 1][j + 1] = 'w'
    if i < len(board_colors) - 1:
        if j > 0:
            is_black(board_colors[i + 1][j - 1])
            board_colors[i + 1][j - 1] = 'w'
        if j < len(board_colors[i]):
            is_black(board_colors[i + 1][j + 1])
            board_colors[i + 1][j + 1] = 'w'


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
                if are_horiz_neigh_diff:
                    paint_neighbors_horizontal_while(i, j, board_colors)


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


def paint_continuous_path(board_colors, i, j):
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
    global is_generate
    if color == 'w':
        if is_generate:
            raise AttributeError
        is_generate = True
        raise AssertionError
        # exit('Головоломку невозможно решить - попытка закрасить черным белую клетку')


def is_black(color):
    global is_generate
    if color == 'b':
        if is_generate:
            raise AttributeError
        is_generate = True
        raise AssertionError
        # exit('Головоломку невозможно решить - попытка закрасить белым черную клетку')


def hitori_solution():
    global is_generate, final_board, final_board_color
    if is_generate:
        board = generate()
    else:
        board = input_board()
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
                            paint_continuous_path(board_colors, i, j)
            if not is_painted:
                break
            if prev_board_colors == board_colors:
                if is_generate:
                    raise AttributeError
                is_generate = True
                raise AssertionError

        final_board = board
        final_board_color = board_colors
        change_flag()
        is_generate = True
    except AttributeError:
        hitori_solution()
    except AssertionError:
        print('Головоломку невозможно решить')


def can_solve():
    global is_generate
    is_generate = False
    hitori_solution()


def find_solution():
    hitori_solution()
    for row in final_board:
        print(row)
    print()
    for row in final_board_color:
        print(row)


def return_board():
    return final_board
